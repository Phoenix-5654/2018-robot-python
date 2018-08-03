from wpilib.command.subsystem import Subsystem


class Grippers(Subsystem):
    MAX_SPEED = 0.7
    MIN_SPEED = -MAX_SPEED

    def __init__(self, left_motor, right_motor):

        super().__init__('Grippers')

        self.left_motor = left_motor
        self.right_motor = right_motor

    def set_motors(self, left_motor_speed, right_motor_speed):

        self.left_motor.set(left_motor_speed)
        self.right_motor.set(right_motor_speed)

    def exhaust(self):
        self.set_motors(self.MIN_SPEED, self.MAX_SPEED)

    def intake(self):
        self.set_motors(self.MAX_SPEED, self.MIN_SPEED)

    def stop(self):

        self.set_motors(0, 0)
