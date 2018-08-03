from wpilib.command import TimedCommand


class TimedExhaust(TimedCommand):

    def __init__(self, timeout_in_sec):
        super().__init__(timeoutInSeconds=timeout_in_sec, name='Timed Exhaust')

        self.requires(self.getRobot().grippers)

    def execute(self):
        self.getRobot().grippers.exhaust()

    def end(self):
        self.getRobot().grippers.stop()
