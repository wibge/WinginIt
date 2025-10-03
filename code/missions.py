from CoopBot import bot

def spinWheels():
    bot.drive_base.drive(200)

def main():
    #bot.front_motor.run_until_stalled(100, Stop.COAST, 50)
    print("Wingin' it")
    #bot.driveStraight(500)
    #bot.followline()
    bot.driveUntilImpact(forward=True)
    #bot.colorPrint()
    print()


main()
