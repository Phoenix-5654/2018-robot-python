from wpilib.command import Command


class GrippersExhaust(Command):

    def __init__(self):

        super().__init__('Grippers Exhaust')

        self.requires(self.getRobot().grippers)

    def initialize(self):

        self.getRobot().grippers.exhaust()

    def end(self):

        self.getRobot().grippers.stop()
