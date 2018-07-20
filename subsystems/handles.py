from wpilib.command.subsystem import Subsystem


class Handles(Subsystem):

    def __init__(self, solenoid):

        super().__init__('Handles')

        self.solenoid = solenoid

    def open(self):

        self.solenoid.set(2)

    def close(self):

        self.solenoid.set(1)

    def state(self):

        return self.solenoid.get()
