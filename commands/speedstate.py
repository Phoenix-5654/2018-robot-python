from wpilib.command import InstantCommand


class SpeedState(InstantCommand):

    def __init__(self):

        super().__init__('Speed State')

        self.requires(self.getRobot().drivetrain)

    def initialize(self):

        print("speed")
        self.getRobot().drivetrain.speed_state()
