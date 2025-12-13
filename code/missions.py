from CoopBot import bot, LEFT, RIGHT, BLACK, WHITE
from pybricks.tools import wait, StopWatch, hub_menu
from pybricks.parameters import Button
from pybricks.parameters import Icon
def spinWheels():
    #this function can be used for wheel cleaning and crossing over-
    #to the other side of the map
    bot.drive_base.drive(600,0)
    wait(600000)
    
def mapReveal():
    bot.backToWall()
    bot.armDown()
    wait(50)
    bot.moveTopArm(100)
    bot.moveArm(50)
    wait(50)


    bot.driveStraight(770,300) # long drive across mat
    wait(50)
    bot.turn(-41)
    wait(50)

    bot.driveStraight(95) # approach model
    bot.topArmDown()
    
    bot.moveArm(100) # lift up grass
    bot.driveStraight(37) # forward, push grass
    bot.moveTopArm(100) # move top arm, so it doesn't get caught on loop
    bot.driveStraight(-210)

    #return home
    bot.turn(70)
    bot.driveStraight(-700, speed=400)

def Morge():
    bot.armDown()
    bot.driveStraight(805)
    bot.turn(-27, timeout=True, timeoutms=2000)
    bot.driveStraight(-5)
    bot.turn(-5, timeout=True, timeoutms=1000)
    wait(500)
    #goingtoforge
    bot.turn(50, timeout=True, timeoutms=2000)
    bot.driveStraight(-55)
    bot.turn(30, timeout=True, timeoutms=2000)
    bot.turn(-10)
    bot.turn(15)
    bot.driveStraight(-100, speed=300)
    #return to home
    bot.turn(-80)
    bot.driveStraight(-700, speed=800)
"""
def whatsonsale9():
    bot.backToWall()
    bot.armDown()
    wait(20)
    bot.moveArm(100)
    bot.driveStraight(290)
    bot.smartTurn(-50)
    
    bot.driveStraight(100)
    
    # head towards next mission
    bot.smartTurn(58.0)
    wait(50)
    bot.armDown()
    bot.driveStraight(420)
    
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
    bot.driveStraight(-700, speed=800)
"""
   
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
    bot.driveStraight(293)
    bot.smartTurn(-90)
    bot.driveStraight(-90)
    bot.armDown()
    bot.driveStraight(60)

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
    
    bot.armDown(armspeed=300) # lowering basket
    bot.armUp()
    bot.driveStraight(-20)
    bot.armDown(armspeed=300)
    bot.armUp()
    bot.driveStraight(-35) #backing up from basket

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
    bot.drive_base.stop()

def YarHarAPiratesLifeForMe():
    bot.armUp()
    bot.driveStraight(-600,speed=450)
    bot.driveStraight(-170,speed=150)
    #bot.driveStraight(600, speed=450)
    bot.drive_base.drive(speed=500, turn_rate=-1) # arc towards home
    wait(3000)
    bot.drive_base.drive(speed=500, turn_rate=-10) # arc towards home
    wait(4000)
    bot.drive_base.stop()

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
    bot.driveStraight(-170) #back up from wall
    bot.turn(-39) # turn towards statue
    bot.driveStraight(105)
    bot.moveArm(-210) # grab statue
    bot.drive_base.settings(straight_speed=400, straight_acceleration=400)
    bot.driveStraight(-90, speed=400)
    bot.turn(20)
    bot.armUp()

    bot.drive_base.drive(speed=-500, turn_rate=0)
    wait(2000)
    bot.drive_base.stop()

def brush():

    bot.armUp()
    bot.driveStraight(distance=500, speed=400)
    bot.moveArm(-207)  
    bot.driveStraight(-80)
    bot.moveArm(200)
    bot.moveArm(-420)
    bot.driveStraight(-70)
    bot.moveArm(-150)
    bot.driveStraight(-70)
    bot.moveArm(100)
    bot.driveUntilImpact(forward=False, speed=300)


def display(number):
    bot.prime_hub.display.char(str(number))

def menu():

    bot.setdefalts()
    x=hub_menu("1","2","3","4","5","6")
    if x=="1":
        spinWheels()
    if x=="2":
        mapReveal()
    if x=="3":
        Morge()
    if x=="4":
        minecarttop()
    if x=="5":
        heavyLifting()
    if x=="6":
        YarHarAPiratesLifeForMe()

def competition_menu():

    bot.prime_hub.system.set_stop_button((Button.LEFT, Button.RIGHT)) 
    bot.setdefalts()
    # Mission order: 2, 4, 3, 5
    mission_order = [1, 2, 6, 4, 3, 5,
                        ]
    mission_functions = {
        1: spinWheels,
        2: mapReveal,
        4: minecarttop,
        3: Morge,
        5: heavyLifting,
        6: YarHarAPiratesLifeForMe
    }   


    current_index = 1
    mission_num = mission_order[current_index]
    display(mission_num)

    while True:
        
        # Display current mission number


        # Wait for button press
        pressed = bot.prime_hub.buttons.pressed()

        if len(pressed) > 0:
            if Button.CENTER in pressed:
                # Start the selected mission
                
                mission_functions[mission_num]()
                current_index = (current_index + 1) % len(mission_order)
                bot.setdefalts()
                 
            elif Button.LEFT in pressed:
                # Move to previous mission in the list
                current_index = (current_index - 1) % len(mission_order)
                wait(200)  # Debounce delay
            elif Button.RIGHT in pressed:
                # Move to next mission in the list
                current_index = (current_index + 1) % len(mission_order)
                wait(200)  # Debounce delay

            mission_num = mission_order[current_index]
            display(mission_num)



        wait(50)  # Small delay to prevent excessive CPU usage

competition_menu()