from CoopBot import bot, LEFT, RIGHT, BLACK, WHITE
from pybricks.tools import wait, StopWatch

def spinWheels():
    bot.drive_base.drive(200,0)
    wait(600000)

def main():
  
    whatsonsale9()
    return
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
    theforge()
    return
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

    #bot.turn(-110)
    #bot.driveStraight(700)

    bot.turn(70)
    bot.driveStraight(-700, speed=400)


def theforge():
    bot.armDown()
    #bot.armUp()
    bot.driveStraight(740)
    #bot.moveArm(20)
    bot.turn(30)
    bot.driveStraight(-75)
    #bot.turn(50)
    #bot.driveUntilImpact()

def whatsonsale9():
    bot.armDown()
    bot.driveStraight(290)
    bot.turn(-45)
    bot.moveArm(100)
    bot.driveStraight(120)
    bot.moveArm(-100)
    bot.moveArm(50)
    bot.armUp()

    # head towards next mission
    bot.turn(57)
    bot.driveStraight(370)
    bot.moveArm(-210)
    
    bot.turn(-30)
    wait(200)
    #goingtoforge
    bot.turn(5)
    bot.driveStraight(-5)
    bot.armDown()
    bot.turn(30)
    return
    bot.moveArm(-100)
     
#this line should always be last
main()