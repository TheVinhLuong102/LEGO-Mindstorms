#!/usr/bin/env pybricks-micropython


from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Port, Stop, Button
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Configure 2 motors with default settings on Ports B and C.  These
# will be the left and right motors of the Driving Base.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# The wheel diameter of the Robot Educator Driving Base is 56 mm.
wheel_diameter = 56

# The axle track is the distance between the centers of each of the
# wheels.  This is 118 mm for the Robot Educator Driving Base.
axle_track = 118

# The Driving Base is comprised of 2 motors.  There is a wheel on each
# motor.  The wheel diameter and axle track values are used to make the
# motors move at the correct speed when you give a drive command.
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# Set up the Touch Sensor on Port 1.  It is used to increase the speed
# of the robot.
increase_touch_sensor = TouchSensor(Port.S1)

# Set up the Touch Sensor on Port 2.  It is used to decrease the speed
# of the robot.
decrease_touch_sensor = TouchSensor(Port.S2)

# Initialize the "old_speed" variable to "None."  It is used to check
# whether the speed variable has changed.  Setting it to "None" ensures
# this check will be "True" when the speed variable is initialized with
# a value.
old_speed = None

# Initialize the speed variable to 0.
speed = 0

# This is the main part of the program.  It is a loop that repeats
# endlessly.
#
# First, increase the speed variable if Touch Sensor 1 is pressed.
# Second, decrease the speed variable if Touch Sensor 2 is pressed.
# Finally, the robot updates its speed if the speed variable was
# changed, and displays it on the screen.
#
# Then the loop starts over after a brief pause.
while True:

    # Check whether Touch Sensor 1 is pressed, and increase the speed
    # variable by 10 mm per second if it is.
    if increase_touch_sensor.pressed():
        speed += 10

    # Check whether Touch Sensor 2 is pressed, and decrease the speed
    # variable by 10 mm per second if it is.
    if decrease_touch_sensor.pressed():
        speed -= 10

    # If the speed variable has changed, update the speed of the robot
    # and display the new speed in the center of the screen.
    if speed != old_speed:
        old_speed = speed
        robot.drive(speed, 0)
        brick.display.clear()
        brick.display.text(speed, (85, 70))

    # Wait 200 milliseconds before starting the loop again.
    wait(200)
