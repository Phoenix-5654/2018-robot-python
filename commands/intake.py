from wpilib.command import Command


class GrippersIntake(Command):

    def __init__(self):

        super().__init__('Grippers Intake')

        self.requires(self.getRobot().grippers)

    def initialize(self):

        self.getRobot().grippers.intake()

    def end(self):

        self.getRobot().grippers.stop()
