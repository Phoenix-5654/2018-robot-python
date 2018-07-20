from commands.followjoystick import FollowJoystick

import wpilib
import wpilib.drive
from wpilib.command.subsystem import Subsystem


class Drivetrain(Subsystem):

    def __init__(self, left, right, solenoid):

        super().__init__('Drivetrain')

        self.drive = wpilib.drive.DifferentialDrive(left, right)
        self.solenoid = solenoid

    def speed_state(self):

        self.solenoid.set(1)

    def strength_state(self):

        self.solenoid.set(2)

    def state(self):

        return self.solenoid.get()

    def drive_robot(self, y_speed, x_speed):

        self.drive.arcadeDrive(y_speed, x_speed)

    def initDefaultCommand(self):

        self.setDefaultCommand(FollowJoystick())
