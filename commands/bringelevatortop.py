from wpilib.command import Command


class BringElevatorTop(Command):

    def __init__(self):
        super().__init__('Bring Elevator Top')

        self.requires(self.getRobot().elevator)

    def execute(self):
        self.getRobot().elevator.motor_up()

    def end(self):
        self.getRobot().elevator.stop()

    def isFinished(self):
        return self.getRobot().elevator.is_at_top()
