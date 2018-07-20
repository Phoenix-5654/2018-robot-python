from wpilib.command import ConditionalCommand


class DrivetrainState(ConditionalCommand):

    def __init__(self, strength_state, speed_state):

        super().__init__('Drivetrain State', strength_state, speed_state)

    def condition(self):

        drivetrain_state = self.getRobot().drivetrain.state()
        return drivetrain_state == 1 or drivetrain_state == 0
