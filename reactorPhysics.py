#!/usr/bin/python

# Contains reactor kenetics equations
# and reactor parameters

beta = 0.0079  # sum delayed neutron precursor frac [unitless]
lamb = 0.08    # delayed neutron precursor time const^-1 [s]
Lamb = 10.e-5  # average neutron lifetime [s]

v = 2200.e3  # neutron velocity cm/s
Ef = 3.204e-11  # energy per fission [J]
Sigma_f = 0.0065  # Macrosopic fission cross section in reactor [1/cm]
Vr = 3.e6  # reactor volumue [cc]
Lc = Lamb * v  # mean nutron travel length in core [cm]
VfFuel = 0.4
VfH2O = 1. - VfFuel

hc = 1.    # W/cm^2 * K avg heat transfer coeff between fuel and water
Ac = 4.e5  # cm^2  fuel to coolant contact area
Tin = 450.  # K coolant inlet temperature

alphaT = -3. * 1.e-5 / beta  # pcm / K / beta  reactivity per kelvin


def dndt(S, t, reactivity):
    """
    Time derivative of neutron population.
    """
    ndot = (reactivity - beta) / Lamb * S[0] + lamb * S[1]
    if S[0] <= 0. and ndot < 0.:
        return 0.
    else:
        return ndot


def dCdt(S, t):
    """
    Time derivative of delayed neutron precursor population.
    """
    Sdot = (beta / Lamb) * S[0] - lamb * S[1]
    if S[1] < 0. and Sdot < 0.:
        return 0.
    else:
        return Sdot


def qFuel(n):
    """
    Given neutron population return thermal power
    """
    return Vr * VfFuel * (n * v) * Sigma_f * Ef


def dTfdt(S, t, mdotC):
    """
    Time derivative of fuel temperature
    """
    CpUO2 = 0.2455  # J/g*K
    densityUO2 = 12.5  # g/cc
    h = hc * (1.e-7 * mdotC + 0.9)  # convective heat transfer coeff dependent on coolant flow rate
    return (qFuel(S[0]) - Ac * h * (S[2] - S[3])) / (densityUO2 * VfFuel * Vr * CpUO2)


def dTcdt(S, t, mdotC):
    """
    Time derivative of water coolant.
    """
    CpH2O = 4.2  # J/g*K
    densityH2O = 1.  # g/cc
    h = hc * (1.e-7 * mdotC + 0.9)
    return (Ac * h * (S[2] - S[3]) + CpH2O * (Tin - S[3]) * mdotC) / (densityH2O * Vr * CpH2O)


def diffRodWorth(h):
    """
    Differential Control rod worth curve.
    h is fractional height:  h=100  is fully withdrawn position
    delta_h * R(h) = reactivity change
    """
    scalingFac = 0.2 * 1.e-5 / beta
    return (0.00175 * h ** 3 - 0.3675 * h ** 2 + 19.450 * h) * scalingFac


def intRodWorth(h1, h2):
    """
    Integral Control rod worth curve.
    """
    scalingFac = 0.2 * 1.e-5 / beta
    integral = lambda h: (0.00175 / 4) * h ** 4 - (0.3675 / 3) * h ** 3 + (19.45 / 2) * h ** 2
    return (integral(h2) - integral(h1)) * scalingFac


def rho(S, t, hrate, deltaT):
    """
    Temperature and control rod reactivity.
    Reactivity in units of Dollars  (deltaK / Beta)
    Takes control rod movement rate in (%/s)
    """
    return alphaT * (S[2] - Tin) + intRodWorth(0., S[4])


def reactorSystem(S, t, hrate, deltaT, mdotC=1000.e3):
    reactivity = rho(S, t, hrate, deltaT)
    return [dndt(S, t, reactivity), dCdt(S, t),
            dTfdt(S, t, mdotC), dTcdt(S, t, mdotC), hrate]
