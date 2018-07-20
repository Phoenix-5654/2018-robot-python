from wpilib.command import InstantCommand


class HandlesOpen(InstantCommand):

    def __init__(self):

        super().__init__('Handles Open')

        self.requires(self.getRobot().handles)

    def initialize(self):

        print("opening")
        self.getRobot().handles.open()
