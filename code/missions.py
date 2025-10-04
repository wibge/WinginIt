from CoopBot import bot, LEFT, RIGHT, BLACK, WHITE
from pybricks.tools import wait, StopWatch

def spinWheels():
    bot.drive_base.drive(200)

def main():
    mapReveal()
    return
    #bot.front_motor.run_until_stalled(100, Stop.COAST, 50)
    print("Wingin' it")
    #bot.driveStraight(500)
    #bot.followline()
    #bot.driveUntilImpact(forward=True)
    #bot.colorPrint()
    print() 
    # HI CALLIOPEß
    bot.armUp()
    bot.armDown()
    
    wait(1000)
    print(bot.front_motor.control.stall_tolerances())
    bot.armUp()
    bot.armDown()

def mapReveal():
    
    bot.armDown()
    bot.moveArm(85)
    bot.moveTopArm(150)

    wait(50)
    bot.driveStraight(780)
    wait(50)
    bot.turn(-50)
    wait(50)

    bot.driveStraight(125)
    bot.topArmDown()
    return
    bot.moveArm(190)
    
    bot.driveStraight(-200)


main()
