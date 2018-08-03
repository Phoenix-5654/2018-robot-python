from wpilib.command import Command


class DriveStraight(Command):

    def __init__(self, distance):
        super().__init__('Drive Straight')

        self.requires(self.getRobot().drivetrain)

        self.distance = self.getRobot().drivetrain.distance_to_ticks(distance)

    def initialize(self):
        self.getRobot().drivetrain.reset_encoder()
        self.getRobot().drivetrain.reset_gyro()
        self.getRobot().drivetrain.enable()
        self.getRobot().drivetrain.setSetpoint(self.distance)

    def execute(self):
        self.getRobot().drivetrain.update_gyro_pid()

    def end(self):
        self.getRobot().drivetrain.disable()

    def isFinished(self):
        return self.getRobot().drivetrain.onTarget()
