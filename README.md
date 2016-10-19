About
-----
Point kinetic reactor model with GUI frontend.

![screenshot](https://github.com/wgurecky/pyReactor/blob/master/simulator_screenshot.png)

Interfaces with an Arduino driven LEGO(R) model (optional).

![image](https://github.com/wgurecky/pyReactor/blob/master/lego_photo_sm.png)

For use as a reactor demo for K-12 students.  This package was developed to inform young students about nuclear engineering.
To this end, a LEGO(R) reactor was constructed for use with the Arduino code.  Control rod movement and reactor power visual
feedbacks are presented to the audience via servo and LED control respectively.



Install
-------

To install:

    python setup.py develop


Requires
   
    python2.7
    numpy
    scipy
    matplotlib
    wxpython
    pyserial


Usage
-----

The main ractor gui program is lauched using the command::

    pyReactor

The reactor may be used in power control mode, in which the reactor will attempt to maintain the user set power.
In standard control rod based mode (pwr control toggle unchecked), the rod position may be set with a vertical slider.
The rods move at a set, relaively slow pace.  The rod height is visualized by a vertical bar plot.

Temperature is plotted as a dimensionless distance to the SCRAM value.  This is done to display both the fuel and moderator
temperature on the same plot.

The scram button will generate a SCRAM event.  To unlock the reactor after a SCRAM, click the SCRAM button again.

An Arduino may be connected.  A simple arduino play is included in this package. The Arduino code controls a small servo
which may be used to raise/lower control rods.  It also drives a (preferably blue) LED to give visual reactor power feedback.


Authors
-------

William Gurecky

william.gurecky@gmail.com

License
-------

Software included in the pyReactor project is distributed under the MIT license.
You should have received a version of the MIT license with this software.  If not,
please refer to <https://opensource.org/licenses/MIT>.
