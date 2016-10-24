# IRobotCreate2Motion
To establish connection:

Find the usb-serial port connected to the robot (```ls /dev/tty.*```) and in Research/IRobotCreate2/breezycreate2/__init__.py, change the port on line 39 to your port.

To run the robot freely:

Go to Research/IRobotCreate2 and run ```python robotest.py [speed] [time]``` where speed is in mm/s and time is in s.

To stop the robot, run ```python robostop.py```, or use Ctrl-C.
