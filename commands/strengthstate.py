from wpilib.command import InstantCommand


class StrengthState(InstantCommand):

    def __init__(self):

        super().__init__('Strength State')

        self.requires(self.getRobot().drivetrain)

    def initialize(self):

        print("strength")
        self.getRobot().drivetrain.strength_state()
