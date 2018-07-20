from wpilib.command.subsystem import Subsystem


class Grippers(Subsystem):

    def __init__(self, left_motor, right_motor):

        super().__init__('Grippers')

        self.left_motor = left_motor
        self.right_motor = right_motor

    def set_motors(_, self, left_motor_speed, right_motor_speed):

        self.left_motor.set(left_motor_speed)
        self.right_motor.set(right_motor_speed)

    def intake(self):

        self.set_motors(self, -0.7, 0.7)

    def exhaust(self):

        self.set_motors(self, 0.7, -0.7)

    def stop(self):

        self.set_motors(self, 0, 0)
