from CoopBot import bot, LEFT, RIGHT, BLACK, WHITE
from pybricks.tools import wait, StopWatch

def spinWheels():
    bot.drive_base.drive(200,0)
    wait(600000)

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
    #bot.turn(45)
    #print(bot.drive_base.heading_control.target_tolerances())
    #return
    #bot.driveStraight(500)
    #return

    bot.armDown()
    wait(20)
    bot.moveTopArm(130)
    wait(20)
    bot.moveArm(50)
    wait(50)

    
    bot.driveStraight(745,150) # long drive across mat
    wait(50)
    bot.turn(-42)
    wait(50)

    bot.driveStraight(155) # approach model
    bot.topArmDown()
    
    bot.moveArm(100)
    bot.driveStraight(-200) # back up 

def theforge():
    bot.armUp()
    bot.driveStraight(740)
    #bot.moveArm(20)
    bot.turn(30)
    bot.driveStraight(-75)
    bot.turn(50)
    bot.driveUntilImpact()
main()
