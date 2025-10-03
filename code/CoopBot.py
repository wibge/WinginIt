from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.parameters import Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

LEFT = 1
RIGHT = 0

BLACK = 1
WHITE = 0


class CoopBot:
    prime_hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
    left_sensor = ColorSensor(Port.D)
    right_sensor = ColorSensor(Port.F)
    top_motor = Motor(Port.A, Direction.CLOCKWISE)
    front_motor = Motor(Port.C, Direction.CLOCKWISE)
    left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.E, Direction.CLOCKWISE)
    # configure drive base with wheel diameter and distance apart
    drive_base = DriveBase(left_motor, right_motor, 56, 94)

    def __init__(self):
        self.drive_base.use_gyro(True)

    


    def isSensorOnColor(self, side, color=BLACK):
        """ Tests if the sensor is on the color

        Args:
            side (int): Use LEFT or RIGHT global variables 
            color (int, optional): color to test for: WHITE or BLACK Defaults to BLACK.

        Returns:
            int: Value will be 0 or negative if the sensor is on the color. If the value is positive and small it is mostly on the color.
        """
        black_cutoff = 8
        white_cutoff = 20
        if color == BLACK:
            if side == LEFT:
                return self.left_sensor.reflection() - black_cutoff
            else: 
                return self.right_sensor.reflection() - black_cutoff
        else: 
            if side == LEFT:
                return white_cutoff - self.left_sensor.reflection() 
            else: 
                return white_cutoff - self.right_sensor.reflection()
            
    def colorPrint(self):
        """ Prints sensor values to help with testing
        """
        print("Left: " + str(self.left_sensor.reflection()) + " " + str(self.left_sensor.hsv()))
        print("Rght: " + str(self.right_sensor.reflection()) + " " + str(self.right_sensor.hsv()))

    def driveStraight(self, distance, speed=100):
        """ Bot drives straight using the gyroscope

        Args:
            distance (int): distance in mm, negative goes backwards
            speed (int, optional): Speed in degrees/s of the wheel motor. Defaults to 100.
        """
 

        # go backwards if distance is negative
        direction = 1 if distance > 0 else -1
        speed = speed * direction

        # resets gyro/heading to zero, resets distance traveled to zero
        self.drive_base.reset()
        wait(10) # wait in millisecond 
        self.drive_base.drive(speed, 0)  # start driving
        
        print("Start: " + str(self.prime_hub.imu.heading()) + " " + str(self.drive_base.distance()))

        # loop while you haven't traveled the full distance
        while self.drive_base.distance() * direction < (distance * direction):
            print(str(self.prime_hub.imu.heading()) + " " + str(self.drive_base.distance()))
            heading = self.prime_hub.imu.heading()
            #self.drive_base.drive(speed, -heading)
            self.drive_base.drive(speed, 0)

        self.drive_base.stop()

    def driveUntilImpact(self, forward=True, speed=100):
        if not forward:
            speed=-speed

        # resets gyro/heading to zero, resets distance traveled to zero
        self.drive_base.reset()
        wait(100) # wait in millisecond 
        self.drive_base.stop()
        wait(100)
        self.drive_base.drive(speed, 0)  # start driving
        
        print("Start: " + str(self.prime_hub.imu.heading()) + " " + str(self.drive_base.distance()))

        # loop while you haven't traveled the full distance
        last_heading = self.prime_hub.imu.heading()
        while True:
            heading = self.prime_hub.imu.heading() 
            print(str(last_heading - heading) + " " + str(self.drive_base.distance()))
 
            if abs(heading - last_heading) > 0.5:
                break

            last_heading = heading
        self.drive_base.stop()   

    def colorCode(self, speed=100):
        self.drive_base.reset()
        self.drive_base.settings(straight_speed=speed)
        self.drive_base.drive(speed, 0)
    
        while not self.isSensorOnColor(LEFT, BLACK):
            print(self.left_sensor.hsv())
            print(self.right_sensor.hsv())
            print(self.left_sensor.reflection())
            print(self.right_sensor.reflection())
            print(str(self.prime_hub.imu.heading()) + " " + str(self.drive_base.distance()))

            heading = self.prime_hub.imu.heading()
            self.drive_base.drive(speed, -heading)
        

        self.drive_base.stop()

    def squareUp(self, speed=100):
        """ Robot drives until it reaches BLACK, and aligns both sensors with the color. 


        Args:
            speed (int, optional): in degrees/s. If negative, robot will go backwards. Defaults to 100.
        """
        self.drive_base.reset()
        self.drive_base.settings(straight_speed=speed)
        self.drive_base.drive(speed, 0)
    
        while True:
            left_sensor_on = self.isSensorOnColor(LEFT, BLACK)
            right_sensor_on = self.isSensorOnColor(RIGHT, BLACK)
            print("L: " + str(self.left_sensor.reflection()) + ", R: " + str(self.right_sensor.reflection()))

            if left_sensor_on <= 0 and right_sensor_on <= 0:
                break


            #print(str(self.prime_hub.imu.heading()) + " " + str(self.drive_base.distance()))
            current_speed = speed
            if left_sensor_on < 5 or right_sensor_on < 5:
                current_speed = max(speed, 25)
            elif left_sensor_on < 8 or right_sensor_on < 8:
                current_speed = max(speed, 50)

 

            if left_sensor_on > 0:
                self.left_motor.run(current_speed)
            else:
                self.left_motor.stop()

            if right_sensor_on > 0:
                self.right_motor.run(current_speed)
            else:
                self.right_motor.stop()

        self.left_motor.stop()
        self.right_motor.stop()
    
    
    def followline(self, speed = 100):
        """ DOES NOT WORK. Robot follows the line with its left sensor

        Args:
            speed (int, optional): _description_. Defaults to 100.
        """
        self.drive_base.reset()
        self.drive_base.settings(straight_speed=speed)
        self.drive_base.drive(speed, 0)
        
        THRESHOLD = 6     # Reflected light intensity threshold for the line (adjust as needed)
        PROPORTIONAL_GAIN = 2 # Adjust for steering sensitivity

        while True:
            left_sensor_on = self.isSensorOnColor(LEFT, BLACK)
            right_sensor_on = self.isSensorOnColor(RIGHT, BLACK)
            print("L: " + str(self.left_sensor.reflection()) + ", R: " + str(self.right_sensor.reflection()))

            current_reflection = bot.left_sensor.reflection()

            # Calculate the deviation from the threshold
            deviation = current_reflection - THRESHOLD

            # Calculate the turn rate based on deviation and proportional gain
            turn_rate = PROPORTIONAL_GAIN * deviation

            current_speed = speed
            if left_sensor_on > 5:
                current_speed = max(speed, 50)
            elif left_sensor_on > 8:
                current_speed = max(speed, 25)

            # Drive the robot
            self.drive_base.drive(current_speed, turn_rate)

            # Optional: add a small delay to control loop speed
            wait(5)
            #print(str(self.prime_hub.imu.heading()) + " " + str(self.drive_base.distance()))
       

            if left_sensor_on > 20:
                break

        self.drive_base.stop()
       

    def armUp(): 
        print(bot.front_motor.control.stall_tolerances())
        bot.front_motor.run_until_stalled(100, Stop.COAST)

    def armDown():
        print(bot.front_motor.control.stall_tolerances())
        bot.front_motor.run_until_stalled(-100, Stop.COAST)   

bot = CoopBot()


