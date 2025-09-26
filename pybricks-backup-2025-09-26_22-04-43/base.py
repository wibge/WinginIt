from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.parameters import Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Set up all devices.
prime_hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
left_sensor = ColorSensor(Port.F)
right_sensor = ColorSensor(Port.D)
top_motor = Motor(Port.A, Direction.CLOCKWISE)
front_motor = Motor(Port.C, Direction.CLOCKWISE)
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)
drive_base = DriveBase(left_motor, right_motor, 56, 94)


# The main program starts here.
def main():
    print(left_sensor.hsv())
    print(right_sensor.hsv())
    print(left_sensor.reflection())
    print(right_sensor.reflection())
    print('Hello, Pybricks!')

    #top_motor.run_angle(360, -1000)
    front_motor.run_until_stalled(100, Stop.COAST, 50)
    wait(500)
    print('up')

    front_motor.run_until_stalled(-100, Stop.COAST, 50)
    wait(500)
    print('down')

    front_motor.run_until_stalled(100, Stop.COAST, 50)
    wait(500)
    print('up')

    front_motor.run_until_stalled(-100, Stop.COAST, 50)
    wait(500)
    print('down')

    front_motor.run_until_stalled(100, Stop.COAST, 50)
    wait(500)
    print('up')

    print('Hello, Pybricks!')


    return
    left_motor.run_angle(360, 720)
    right_motor.run_angle(360, 720)
    drive_base.straight(1000)

main()