from wpilib.command import ConditionalCommand


class HandlesState(ConditionalCommand):

    def __init__(self, handles_open, handles_close):

        super().__init__('Handles State', handles_open, handles_close)

    def condition(self):

        handles_state = self.getRobot().handles.state()
        return handles_state == 1 or handles_state == 0
