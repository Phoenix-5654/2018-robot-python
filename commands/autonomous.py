from wpilib import DriverStation
from wpilib.command import CommandGroup

from commands.bringelevatorbot import BringElevatorBot
from commands.bringelevatortop import BringElevatorTop
from commands.drivestraight import DriveStraight
from commands.rotatedegrees import RotateDegrees
from commands.strengthstate import StrengthState
from commands.timedexhaust import TimedExhaust
from commands.timedintake import TimedIntake


class AutonomousProgram(CommandGroup):

    def __init__(self):

        super().__init__('Autonomous Program')

        # This gets the alliance color (blue/red) from the driver station
        self.color = DriverStation.getInstance().getAlliance()

        # This gets the robot station (1-3) from the driver station
        self.station = DriverStation.getInstance().getLocation()

        # This gets the switch position (left/right) from the driver station
        self.switch_position = \
            DriverStation.getInstance().getGameSpecificMessage()

        # This checks whether a game specific message was actually sent
        if len(self.switch_position) > 0:
            self.switch_position = self.switch_position[0]

        self.choose_autonomous()

    def choose_autonomous(self):
        """This function chooses between different autonomous modes based on
           the alliance color, robot position and switch position."""
        self.addSequential(StrengthState())

        if self.color == DriverStation.Alliance.Blue:

            if self.station == 2:

                if self.switch_position == 'L':

                    self.b2l_autonomous()

    def b2l_autonomous(self):
        """This is the autonomous corresponding to the blue alliance, 2nd
           position and left switch position"""

        self.addSequential(DriveStraight(170))
        self.addSequential(RotateDegrees(-90))
        self.addSequential(DriveStraight(147))
        self.addParallel(BringElevatorTop())
        self.addSequential(RotateDegrees(90))
        self.addSequential(DriveStraight(105))
        self.addSequential(TimedExhaust(1))
        self.addSequential(DriveStraight(-105))
        self.addParallel(BringElevatorBot())
        self.addSequential(RotateDegrees(46))
        self.addParallel(TimedIntake(10))
        self.addSequential(DriveStraight(150))
