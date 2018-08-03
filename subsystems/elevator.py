from wpilib.command.subsystem import Subsystem


class Elevator(Subsystem):
    UP_SPEED = 0.7
    DOWN_SPEED = -UP_SPEED

    def __init__(self, motor, top_switch, bot_switch):

        super().__init__('Elevator')

        self.motor = motor
        self.top_switch = top_switch
        self.bot_switch = bot_switch

    def up(self):

        if not self.is_at_top():
            self.motor_up()

    def down(self):

        if not self.is_at_bot():
            self.motor_down()

    def motor_up(self):

        self.motor.set(self.UP_SPEED)

    def motor_down(self):

        self.motor.set(self.DOWN_SPEED)

    def is_at_top(self):

        return self.top_switch.get()

    def is_at_bot(self):

        return self.bot_switch.get()

    def stop(self):

        self.motor.set(0)
