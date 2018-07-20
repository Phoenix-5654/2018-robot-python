from wpilib.command import Command


class ElevatorUp(Command):

    def __init__(self):

        super().__init__('Elevator Up')

        self.requires(self.getRobot().elevator)

    def initialize(self):

        self.getRobot().elevator.up()

    def end(self):

        self.getRobot().elevator.stop()
