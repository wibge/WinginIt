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

FRONT_ARM_SPEED = 200
TURN_SPEED = 100
TURN_ACCELERATION = 400
SPEED = 200
SPEED_ACCELERATION = 400
class CoopBot:


    def __init__(self):
        self.prime_hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
        self.left_sensor = ColorSensor(Port.D)
        self.right_sensor = ColorSensor(Port.F)
        self.top_motor = Motor(Port.A, Direction.CLOCKWISE)
        self.front_motor = Motor(Port.C, Direction.CLOCKWISE)
        self.left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.E, Direction.CLOCKWISE)
        # configure drive base with wheel diameter and distance apart
        self.drive_base = DriveBase(self.left_motor, self.right_motor, 56, 94)
        self.front_motor.control.stall_tolerances(speed=100, time=100)
        self.top_motor.control.stall_tolerances(speed=100, time=50)
        self.drive_base.use_gyro(True)
        print(self.drive_base.settings())
        self.drive_base.settings(straight_speed=SPEED, 
                                 straight_acceleration=SPEED_ACCELERATION,
                                 turn_rate=TURN_SPEED,
                                 turn_acceleration=TURN_ACCELERATION)

    def turn(self, angle):
        degrees = angle # make positive rotation clockwise
        max_pct = 30
        feedforward = 5
        p_gain = 0.15
        stop_error = 0.3
        self.drive_base.reset()
        wait(5)
        error = degrees
        velocity = 0
        wheel_pct = 0
        while stop_error < abs(error):
            wheel_pct = int(min(max_pct, feedforward + abs(error * p_gain)))
            direction = 1 if error > 0 else -1
            velocity = -direction * (wheel_pct * TURN_SPEED)//100
            self.drive_base.drive(0, velocity)
            error = degrees - self.prime_hub.imu.heading()
        
        self.drive_base.stop()
        wait(10)
            
        print("FINAL wheel_pct:%d        error:%f    yaw_angle:%f    velocity:%f" % (wheel_pct, error, self.prime_hub.imu.heading(), velocity))
        self.drive_base.turn(angle)

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

    def driveStraight(self, distance, speed=SPEED):
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

        totalDistance = distance * direction
        drivenDistance = 0
        # loop while you haven't traveled the full distance
        while drivenDistance < totalDistance:
            #print(str(self.prime_hub.imu.heading()) + " " + str(self.drive_base.distance()))
            #heading = self.prime_hub.imu.heading()
            drivenDistance = self.drive_base.distance() * direction
            remaining_distance = totalDistance - drivenDistance
            # slow down for last 5 cm
            if remaining_distance < 50:
                self.drive_base.drive(speed * remaining_distance/75.0, 0)
            wait(5)
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
       

    def armUp(self): 
        print(self.front_motor.control.stall_tolerances())
        self.front_motor.run_until_stalled(FRONT_ARM_SPEED, Stop.COAST)

    def armDown(self):
        print(self.front_motor.control.stall_tolerances())
        self.front_motor.run_until_stalled(-FRONT_ARM_SPEED, Stop.COAST)   

    def moveArm(self, degrees):
        self.front_motor.run_angle(speed=FRONT_ARM_SPEED, rotation_angle=degrees)

    def moveTopArm(self, degrees):
        self.top_motor.run_angle(speed=FRONT_ARM_SPEED, rotation_angle=degrees)

    def topArmDown(self):
            print(self.top_motor.control.stall_tolerances())
            self.top_motor.run_until_stalled(-FRONT_ARM_SPEED, Stop.COAST)  

    def topArmUp(self):
            print(self.top_motor.control.stall_tolerances())
            self.top_motor.run_until_stalled(FRONT_ARM_SPEED, Stop.COAST)   
bot = CoopBot()


