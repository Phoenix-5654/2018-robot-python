from wpilib.buttons import Trigger


class POVButton(Trigger):

    def __init__(self, joystick, direction):

        super().__init__("POV Button")
        self.joystick = joystick
        self.direction = direction

    def get(self):

        return self.joystick.getPOV() == self.direction
