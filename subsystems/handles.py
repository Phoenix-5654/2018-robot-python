from wpilib.command.subsystem import Subsystem


class Handles(Subsystem):
    CLOSE = 1
    OPEN = 2

    def __init__(self, solenoid):
        super().__init__('Handles')

        self.solenoid = solenoid

    def close(self):
        """This function closes the handles"""
        self.solenoid.set(self.CLOSE)

    def open(self):
        """This function opens the handles"""
        self.solenoid.set(self.OPEN)

    def state(self):
        """This function returns the handles state (open/closed)"""

        return self.solenoid.get()
