from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()
front_motors = MotorPair('A', 'B')
back_motors = MotorPair('E', 'F')

# Custom Functions
def stopMotors():
    front_motors.stop()
    back_motors.stop()

def moveMotors (seconds:float, steer:int, power:int):
    front_motors.start(steer, power)
    back_motors.start(steer, power)
    wait_for_seconds(seconds)
    stopMotors()

def moveSideways (seconds:float, steer:int, power:int):
    """Negative values make it turn left"""
    front_motors.start(steer, power)
    back_motors.start(steer, power*-1)
    wait_for_seconds(seconds)
    stopMotors()


# Write your program here.
hub.speaker.beep()
moveSideways(2, 100, 100)
