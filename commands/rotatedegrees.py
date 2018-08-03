from numpy import sign
from wpilib.command import Command


class RotateDegrees(Command):
    ROTATE_SPEED = 0.4

    def __init__(self, degrees):
        super().__init__('Rotate Degrees')

        self.degrees = degrees

    def initialize(self):
        self.getRobot().drivetrain.reset_gyro()

    def execute(self):
        self.getRobot().drivetrain.drive_robot(0,
                                               self.ROTATE_SPEED *
                                               sign(self.degrees))

    def end(self):
        self.getRobot().drivetrain.drive_robot(0, 0)

    def isFinished(self):
        return abs(self.getRobot().drivetrain.get_gyro_angle()) > \
               abs(self.degrees)
