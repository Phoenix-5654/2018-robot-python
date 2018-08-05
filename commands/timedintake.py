from wpilib.command import TimedCommand


class TimedIntake(TimedCommand):

    def __init__(self, timeout_in_sec):
        super().__init__(timeoutInSeconds=timeout_in_sec, name='Timed Intake')

        self.requires(self.getRobot().grippers)

    def execute(self):
        self.getRobot().grippers.intake()

    def end(self):
        self.getRobot().grippers.stop()
