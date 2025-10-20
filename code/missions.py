from CoopBot import bot, LEFT, RIGHT, BLACK, WHITE
from pybricks.tools import wait, StopWatch, hub_menu

def spinWheels():
    bot.drive_base.drive(200,0)
    wait(600000)

def turnTest():
    bot.armUp()
    wait(1000)
    bot.armDown()
    wait(1000)
    bot.armUp()
    wait(1000)
    bot.armDown()
    wait(1000)

    return
    bot.prime_hub.imu.settings()
    print(bot.drive_base.heading_control.target_tolerances())
    bot.drive_base.heading_control.target_tolerances(speed=29, position=15) 
    print(bot.drive_base.heading_control.pid())
    #bot.drive_base.heading_control.pid(kd=1000, integral_deadzone=4)
    #bot.drive_base.heading_control.
    print(bot.drive_base.heading_control.target_tolerances())
   
    bot.turn(360, timeout=True, timeoutms=20000)
    #bot.turn(90, timeout=True, timeoutms=2000)
    #bot.turn(90, timeout=True, timeoutms=2000)

def main():
    menu()


    turnTest()
    return
    whatsonsale9()

    return
    mapReveal()
    return
    turnTest()
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
    bot.turn(58)
    bot.driveStraight(360)
    bot.moveArm(-210)
    
    bot.turn(-30)
    bot.drive_base.turn(-30, wait = False)
    wait(150)
    bot.drive_base.brake()
    bot.drive_base.stop()
    wait(20)
    #goingtoforge
    bot.turn(10)
    bot.moveArm(30)
    bot.turn(10)
    bot.driveStraight(-30)
    bot.armDown()
    return
    bot.driveStraight(-8)
    bot.moveArm(-100)
    bot.drive_base.turn(40, wait = False)
    wait(150)
    bot.drive_base.stop()
    wait(20)
    bot.driveStraight(-10)


    return
    bot.moveArm(-100)
    
turnTest()
#this line should always be last
#main()
#menu()
def menu():
    x=hub_menu("1","2","3")
    if x=="1":
        spinWheels()
    if x=="2":
        mapReveal()
    if x=="3":
        whatsonsale9()