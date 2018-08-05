from wpilib.command.subsystem import Subsystem


class Grippers(Subsystem):
    MAX_SPEED = 0.7
    MIN_SPEED = -MAX_SPEED

    def __init__(self, left_motor, right_motor):
        super().__init__('Grippers')

        self.left_motor = left_motor
        self.right_motor = right_motor

    def set_motors(self, left_motor_speed, right_motor_speed):
        """
        This function set's the motors output percentage to the given values.
        :param left_motor_speed: the left motor percentage
        :param right_motor_speed: the right motor percentage
        """
        self.left_motor.set(left_motor_speed)
        self.right_motor.set(right_motor_speed)

    def exhaust(self):
        """This function sets the motors values to exhaust an object"""
        self.set_motors(self.MIN_SPEED, self.MAX_SPEED)

    def intake(self):
        """This function sets the motors values to intake an object"""
        self.set_motors(self.MAX_SPEED, self.MIN_SPEED)

    def stop(self):
        """This function stops the motors"""
        self.set_motors(0, 0)
