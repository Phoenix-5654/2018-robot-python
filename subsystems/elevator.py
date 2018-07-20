from wpilib.command.subsystem import Subsystem


class Elevator(Subsystem):

    def __init__(self, motor, top_switch, bot_switch):

        super().__init__('Elevator')

        self.motor = motor
        self.top_switch = top_switch
        self.bot_switch = bot_switch

    def up(self):

        if not self.top_switch.get():

            self.motor.set(0.7)

    def down(self):

        if not self.bot_switch.get():

            self.motor.set(-0.7)

    def stop(self):

        self.motor.set(0)
