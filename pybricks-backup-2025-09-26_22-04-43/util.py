from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from CoopBot import bot

def main():
    #bot.front_motor.run_until_stalled(100, Stop.COAST, 50)
    print("Wingin' it")
    #bot.front_motor.run(100)
    #wait(1000000)
    bot.front_motor.control.stall_tolerances(speed=1, time=1)
    bot.armDown()


    




main()
