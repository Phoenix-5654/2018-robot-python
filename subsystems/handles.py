from wpilib.command.subsystem import Subsystem


class Handles(Subsystem):
    CLOSE = 1
    OPEN = 2

    def __init__(self, solenoid):

        super().__init__('Handles')

        self.solenoid = solenoid

    def close(self):
        self.solenoid.set(self.CLOSE)

    def open(self):
        self.solenoid.set(self.OPEN)

    def state(self):

        return self.solenoid.get()
