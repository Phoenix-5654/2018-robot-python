from wpilib.command import Command


class ElevatorDown(Command):

    def __init__(self):

        super().__init__('Elevator Down')

        self.requires(self.getRobot().elevator)

    def initialize(self):

        self.getRobot().elevator.down()

    def end(self):

        self.getRobot().elevator.stop()
