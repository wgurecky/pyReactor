import numpy as np
from scipy import integrate
from reactorPhysics import reactorSystem
from reactorPhysics import qFuel
from reactorPhysics import rho
#import matplotlib.pyplot as pl
import time


class LegoReactor(object):
    """
    Provides methods to interact with the point kenetics model.
    The reactor system state vector:
    S = [neutrons/cc, pecursors/cc, fuelT, coolantT, rodPosition]
    """
    def __init__(self, initialSystemState=[5.e7, 5.e7, 450., 450., 0.], tstep=0.01):
        """ Initilize reactor system state """
        self.S = initialSystemState
        self.reactivity = rho(self.S, 0, 0, 0)
        self.tstep = tstep
        self.t = np.array([0, self.tstep])
        self.hrate = 0.0  # rod movement rate [% / s]
        self.rodSetPoint = 0.0  # initial rod setpoint [%]
        self.mdotC = 1000.e3  # coolant flow rate [g / s]
        self.coolantSetPoint = 1000.e3
        self.pwrCtrl = False
        self.scramToggle = False
        # For Storage/Plotting
        self.maxTime = 100.  # maximum time storage history [s]
        dataStorLength = self.maxTime / self.tstep
        self.time = np.zeros(dataStorLength)
        self.storVals = np.zeros((5, dataStorLength))

    def timeStep(self):
        """ Step reactor system forward in time """
        self.__preStep()
        self.S = integrate.odeint(reactorSystem, self.S, self.t,
                                  args=(self.hrate, self.tstep, self.mdotC))[-1]
        self.reactivity = rho(self.S, 0, 0, 0)
        self.t += self.tstep
        self.storVals = np.roll(self.storVals, -1, axis=1)
        self.time = np.roll(self.time, -1)
        self.time[-1] = self.t[-1]
        self.storVals[:, -1] = np.array([self.S])

    def __preStep(self):
        """
        Check for valid rod movements or SCRAM condition
        """
        if self.pwrCtrl:
            self.__controlPID()
        else:
            self.__rodCtrl()
        if self.hrate < 0 and self.S[4] <= 0.:
            # do not allow control rods below 0
            self.hrate = 0.
        elif self.hrate > 0 and self.S[4] >= 100.:
            self.hrate = 0.
        self.__controlCoolantRate()
        self.__scramCheck()
        if self.scramToggle:
            # Insert control rods all the way
            self.S[4] = 0.
            self.hrate = 0.

    def __scramCheck(self):
        """
        Check for conditions which require us to SCRAM
        """
        if self.S[2] > 1700:
            # Fuel temp scram (Temp in Kelvin)
            print("Fuel Temperature SCRAM setpoint Exceeded")
            self.SCRAM()
        elif self.S[3] > 700:
            # Coolant temp scram
            print("Coolant Temperature SCRAM setpoint Exceeded")
            self.SCRAM()
        else:
            pass

    def setTimeStep(self, tstep):
        self.tstep = tstep

    def setRodRate(self, rodRate):
        if not self.pwrCtrl:
            self.hrate = rodRate

    def setRodPosition(self, rodPos):
        self.rodSetPoint = rodPos

    def setCoolantRate(self, mdotCin):
        self.coolantSetPoint = mdotCin

    def __controlCoolantRate(self):
        diff = (self.coolantSetPoint - self.mdotC) / 10.
        fnDiff = np.tanh(1.0 * abs(diff))  # Relax control rod into position
        if self.coolantSetPoint > self.mdotC:
            self.mdotC += 1. / self.tstep * fnDiff
        elif self.coolantSetPoint < self.mdotC:
            self.mdotC -= 1. / self.tstep * fnDiff
        else:
            pass

    def togglePwrCtrl(self, pwrSet, pwrCtrlToggle=True):
        """
        Set power in MW
        """
        self.pwrSet = pwrSet
        self.pwrCtrl = pwrCtrlToggle
        self.pidBias = 0.0
        self.hrate = 0.0

    def __controlPID(self):
        maxRate = 1.  # maxumum rod movement rate in %/s
        Kp = 0.000005   # Proportional tunable const
        Ki = 0.0000004  # Intergral tunable const
        Kd = 0.0000005  # Derivitive tunable const
        currentpwr = qFuel(self.S[0]) / 1.e6
        errorFn = self.pwrSet - qFuel(self.storVals[0, :]) / 1.e6
        errorIntegral = np.sum(errorFn[-100:])  # base integral error on past 100 values
        errorDerivative = (errorFn[-1] - errorFn[-2]) / (self.tstep)
        if hasattr(self, 'pwrSet'):
            pidOut = self.pidBias + Kp * (self.pwrSet - currentpwr) + Ki * errorIntegral + Kd * errorDerivative
            self.hrate += pidOut
            if abs(self.hrate) > maxRate:
                self.hrate = maxRate * (self.hrate / abs(self.hrate))
        else:
            self.togglePwrCtrl(qFuel(self.S[0]) / 1.e6)

    def __rodCtrl(self):
        diff = self.S[4] - self.rodSetPoint
        fnDiff = np.tanh(1.0 * abs(diff))  # Relax control rod into position
        if diff < 0.:
            self.hrate = 0.5 * fnDiff
        elif diff > 0.:
            self.hrate = -0.5 * fnDiff
        else:
            self.hrate = 0.

    def SCRAM(self, scramToggle=True):
        """
        You crashed the reactor.
        """
        self.scramToggle = scramToggle


def test():
    """
    Test reactor in rod control and power control modes.
    """
    i = 0
    t0 = time.time()
    legoReactor = LegoReactor()
    legoReactor.setRodPosition(50.)  # set rod position to 50% withdrawn
    while i < 10000:
        legoReactor.timeStep()
        print("===================================")
        print("Time [s] = %f" % legoReactor.t[-1])
        print("Rod percent Withdrawn = %f" % legoReactor.S[4])
        print("Reactor Power [MW] = %f " % float(qFuel(legoReactor.S[0]) / 1.e6))
        print("Tfuel [K] = %f ,  Tcoolant [K] = %f" % (legoReactor.S[2], legoReactor.S[3]))
        i += 1
    i = 0
    legoReactor.togglePwrCtrl(200.)  # set reactor power to 200 MW
    while i < 10000:
        legoReactor.timeStep()
        print("===================================")
        print("Time [s] = %f" % legoReactor.t[-1])
        print("Rod percent Withdrawn = %f" % legoReactor.S[4])
        print("Reactor Power [MW] = %f " % float(qFuel(legoReactor.S[0]) / 1.e6))
        print("Tfuel [K] = %f ,  Tcoolant [K] = %f" % (legoReactor.S[2], legoReactor.S[3]))
        i += 1
    t1 = time.time()
    print(t1 - t0)

if __name__ == "__main__":
    test()
