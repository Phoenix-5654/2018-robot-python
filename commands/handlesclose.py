from wpilib.command import InstantCommand


class HandlesClose(InstantCommand):

    def __init__(self):

        super().__init__('Handles Close')

        self.requires(self.getRobot().handles)

    def initialize(self):

        print("closing")
        self.getRobot().handles.close()
