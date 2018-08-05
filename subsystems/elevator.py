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
        """This function sets the motor's values to push the elevator up, if
           the top switch is not pressed."""

        if not self.is_at_top():
            self.motor_up()

    def down(self):
        """This function sets the motor's values to push the elevator down, if
           the bottom switch is not pressed."""

        if not self.is_at_bot():
            self.motor_down()

    def motor_up(self):
        """This function sets the motor's values to pus the elevator up"""

        self.motor.set(self.UP_SPEED)

    def motor_down(self):
        """This function sets the motor's values to pus the elevator down"""

        self.motor.set(self.DOWN_SPEED)

    def is_at_top(self):
        """
        This function returns whether the elevator has reached the top
        :return: whether the top switch is pressed.
        :rtype: bool
        """

        return self.top_switch.get()

    def is_at_bot(self):
        """
        This function returns whether the elevator has reached the bottom
        :return: whether the bottom switch is pressed.
        :rtype: bool
        """

        return self.bot_switch.get()

    def stop(self):
        """This function stops the elevator"""

        self.motor.set(0)
