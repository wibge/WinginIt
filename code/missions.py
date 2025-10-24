from CoopBot import bot, LEFT, RIGHT, BLACK, WHITE
from pybricks.tools import wait, StopWatch, hub_menu

def spinWheels():
    #this function can be used for wheel cleaning and crossing over-
    #to the other side of the map
    bot.armUp()
    bot.drive_base.drive(600,0)
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


def mapReveal():
    bot.backToWall()
    bot.armDown()
    bot.topArmDown()
    wait(200)
    bot.moveTopArm(200)
    bot.moveArm(50)
    wait(50)

    
    bot.driveStraight(785,150) # long drive across mat
    wait(50)
    bot.smartTurn(-40)
    wait(50)

    bot.driveStraight(95) # approach model
    bot.topArmDown()
    
    bot.moveArm(100) # lift up grass
    bot.driveStraight(-30) # back up, flip switch
    bot.moveTopArm(100) # move top arm, so it doesn't get caught on loop
    bot.driveStraight(-170)

    #return home
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
    bot.backToWall()
    bot.armDown()
    bot.driveStraight(290)
    bot.smartTurn(-45)
    bot.moveArm(100)
    bot.driveStraight(110)
    bot.moveArm(-120, heavy=True)
    bot.moveArm(50)
    bot.armUp()

    # head towards next mission
    bot.smartTurn(56)
    bot.armDown()
    #bot.moveArm(-205)
    bot.driveStraight(430)
    #bot.moveArm(-205)
    
    bot.turn(-25, timeout=True, timeoutms=2000)
    bot.driveStraight(-5)
    bot.turn(-5, timeout=True, timeoutms=1000)
    wait(500)
    #goingtoforge
    bot.turn(50, timeout=True, timeoutms=2000)
    bot.driveStraight(-50)
    bot.turn(30, timeout=True, timeoutms=2000)

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
    
def minecarttop():
    bot.armUp()
    bot.driveStraight(770)
    bot.smartTurn(90)
    bot.driveStraight(335)
    bot.smartTurn(-90)
    bot.driveStraight(-150)
    bot.armDown()
    bot.driveStraight(130)

    #lifting minecart
    bot.moveArm(100, heavy=True)
    bot.driveStraight(5)
    bot.moveArm(60, heavy=True)
    bot.driveStraight(10)
    bot.moveArm(20, heavy=True)
    bot.driveStraight(30)
    bot.moveArm(20, heavy=True)
    bot.driveStraight(35)
    wait(2000)

    bot.driveStraight(-45)
    bot.armUp()

    bot.smartTurn(90)
    bot.driveStraight(560)
    bot.smartTurn(90)
    bot.driveStraight(-30)
    
    bot.armDown() # lowering basket
    bot.armUp()
    bot.driveStraight(-75) #backing up from basket

    #trying to lift platform
    #bot.turn(-45)
    #bot.driveStraight(275, speed=100)

    # returning to launch area
    bot.smartTurn(-70)

    bot.drive_base.arc(700, angle=90)


def menu():
    x=hub_menu("1","2","3","4")
    if x=="1":
        spinWheels()
    if x=="2":
        mapReveal()
    if x=="3":
        whatsonsale9()
    if x=="4":
        minecarttop()
menu()