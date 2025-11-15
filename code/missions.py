from CoopBot import bot, LEFT, RIGHT, BLACK, WHITE
from pybricks.tools import wait, StopWatch, hub_menu

def spinWheels():
    #this function can be used for wheel cleaning and crossing over-
    #to the other side of the map
    bot.drive_base.drive(600,0)
    wait(600000)
    



def mapReveal():
    bot.armDown()
    #bot.topArmDown()
    wait(100)
    bot.moveTopArm(50)
    bot.moveArm(50)
    wait(50)


    bot.driveStraight(780,150) # long drive across mat
    wait(50)
    bot.turn(-41)
    wait(50)

    bot.driveStraight(95) # approach model
    bot.topArmDown()
    
    bot.moveArm(100) # lift up grass
    bot.driveStraight(30) # forward, push grass
    bot.moveTopArm(100) # move top arm, so it doesn't get caught on loop
    bot.driveStraight(-210)

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
    wait(20)
    bot.moveArm(100)
    bot.driveStraight(290)
    bot.smartTurn(-46)
    
    bot.driveStraight(102)
    bot.moveArm(-120, heavy=True)
    bot.moveArm(50)
    bot.driveStraight(-20)
    bot.armUp()
    bot.driveStraight(20)

    # head towards next mission
    bot.smartTurn(56.0)
    wait(50)
    bot.armDown()
    #bot.moveArm(-205)
    bot.driveStraight(420)
    #bot.moveArm(-205)
    
    bot.turn(-27, timeout=True, timeoutms=2000)
    bot.driveStraight(-5)
    bot.turn(-5, timeout=True, timeoutms=1000)
    wait(500)
    #goingtoforge
    bot.turn(50, timeout=True, timeoutms=2000)
    bot.driveStraight(-50)
    bot.turn(30, timeout=True, timeoutms=2000)
    bot.turn(-10)
    bot.turn(15)
    bot.driveStraight(-100, speed=300)
    #return to home
    bot.turn(-80)
    bot.driveStraight(-700, speed=600)



   
    
def minecarttop():
    bot.drive_base.settings(straight_speed=400, 
                        straight_acceleration=150,
                        turn_rate=300,
                        turn_acceleration=400)
    bot.backToWall()
    bot.armUp()
    bot.driveStraight(755)
    wait(50)
    bot.smartTurn(90)
    bot.driveStraight(300)
    bot.smartTurn(-90)
    bot.driveStraight(-90)
    bot.armDown()
    bot.driveStraight(55)

    #lifting minecart
    bot.moveArm(100, heavy=True)
    bot.driveStraight(5)
    bot.moveArm(60, heavy=True)
    bot.driveStraight(10)
    bot.moveArm(20)
    bot.driveStraight(35)
    bot.moveArm(20)
    bot.driveStraight(25)
    wait(100)

    bot.driveStraight(-30)

    bot.armUp()

    bot.smartTurn(87)
    bot.driveStraight(570)
    bot.turn(90)
    bot.driveStraight(-25)
    
    bot.armDown() # lowering basket
    bot.armUp()
    bot.driveStraight(-55) #backing up from basket

    #trying to lift platform
    #bot.turn(-45)
    #bot.driveStraight(275, speed=100)

    # returning to launch area
    bot.turn(-85)
    bot.drive_base.drive(speed=500, turn_rate=5) # straightish to miss red thing
    wait(1000)
    bot.prime_hub.display.char("A")
    bot.drive_base.drive(speed=500, turn_rate=35) # arc towards home
    wait(1500)
    bot.prime_hub.display.char("B")
    bot.drive_base.drive(speed=500, turn_rate=0) # straight in
    wait(1000)

def turntest():
    bot.armUp()
    bot.smartTurn(90)
    wait(1000)
    bot.smartTurn(90)
    wait(1000)
    bot.smartTurn(90)
    wait(1000)
    bot.smartTurn(90)
    wait(1000)

def hometest():
    bot.drive_base.settings(straight_speed=400, 
                straight_acceleration=150,
                turn_rate=300,
                turn_acceleration=400)

   
def heavyLifting():
    bot.armUp()
    bot.drive_base.drive(350, 0)
    wait(4800)
    bot.drive_base.stop()
    bot.drive_base.brake()
    wait(100)
    bot.driveStraight(-150)
    bot.turn(-38)
    bot.driveStraight(70)
    bot.moveArm(-210)
    bot.drive_base.settings(straight_speed=400, straight_acceleration=400)
    bot.driveStraight(-90, speed=400)
    bot.setdefalts()
    bot.turn(20)
    bot.armUp()
    bot.driveStraight(-500)


    #bot.driveStraight(645)
    #bot.turn(45)

    return

def menu():
    bot.setdefalts()
    x=hub_menu("1","2","3","4", "5")
    if x=="1":
        spinWheels()
    if x=="2":
        mapReveal()
    if x=="3":
        whatsonsale9()
    if x=="4":
        minecarttop()
    if x=="5":
        heavyLifting()
menu()