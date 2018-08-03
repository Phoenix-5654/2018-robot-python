from wpilib import DriverStation
from wpilib.command import CommandGroup

from commands.bringelevatorbot import BringElevatorBot
from commands.bringelevatortop import BringElevatorTop
from commands.drivestraight import DriveStraight
from commands.rotatedegrees import RotateDegrees
from commands.strengthstate import StrengthState
from commands.timedexhaust import TimedExhaust


class AutonomousProgram(CommandGroup):

    def __init__(self):

        super().__init__('Autonomous Program')

        self.color = DriverStation.getInstance().getAlliance()

        self.station = DriverStation.getInstance().getLocation()

        self.switch_position = \
            DriverStation.getInstance().getGameSpecificMessage()

        if len(self.switch_position) > 0:
            self.switch_position = self.switch_position[0]

        self.choose_autonomous()

    def choose_autonomous(self):

        self.addSequential(StrengthState())

        if self.color == DriverStation.Alliance.Blue:

            if self.station == 2:

                if self.switch_position == 'L':
                    self.b2l_autonomous()

    def b2l_autonomous(self):

        self.addSequential(DriveStraight(55.5))
        self.addSequential(RotateDegrees(-90))
        self.addSequential(DriveStraight(154))
        self.addParallel(BringElevatorTop())
        self.addSequential(RotateDegrees(90))
        self.addSequential(DriveStraight(231))
        self.addSequential(TimedExhaust(1))
        self.addSequential(DriveStraight(-231))
        self.addParallel(BringElevatorBot())
        self.addSequential(RotateDegrees(45))
        self.addSequential(DriveStraight(40))
