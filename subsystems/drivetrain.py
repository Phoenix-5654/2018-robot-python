import math

import wpilib
import wpilib.drive
from wpilib.command import PIDSubsystem


class Drivetrain(PIDSubsystem):
    WHL_DIAMETER = 15.24
    WHL_CIRC = WHL_DIAMETER * math.pi

    ENCODER_RES = 1024

    QUAD_MULTIPLIER = 4

    STRENGTH_GEAR_RATIO = 16.5

    DIST_TO_TICKS = WHL_CIRC / (ENCODER_RES * QUAD_MULTIPLIER *
                                STRENGTH_GEAR_RATIO)

    SPD_STATE = 1
    STR_STATE = 2

    TIMEOUT_MS = 30

    MAX_SPEED = 0.5
    MIN_SPEED = -MAX_SPEED

    KP = 0.067

    def __init__(self, left, right, solenoid, gyro, encoding_motor):
        super().__init__(0.002, 0, 0, name='Drivetrain')

        self.drive = wpilib.drive.DifferentialDrive(left, right)
        self.solenoid = solenoid
        self.gyro = gyro
        self.encoding_motor = encoding_motor

        self.turn_power = 0

        self.ABS_TOLERANCE = self.distance_to_ticks(3)

        self.encoding_motor.setSensorPhase(True)

        self.setOutputRange(self.MIN_SPEED, self.MAX_SPEED)
        self.setAbsoluteTolerance(self.ABS_TOLERANCE)

    def speed_state(self):
        """This function sets the drivetrain to speed state"""
        self.solenoid.set(self.SPD_STATE)

    def strength_state(self):
        """This function sets the drivetrain to strength state"""
        self.solenoid.set(self.STR_STATE)

    def state(self):
        """This function returns the drivetrain state"""
        return self.solenoid.get()

    def drive_robot(self, y_percent, x_percent):
        """
        This function drives the robot based on given y and x motor output
        values.
        :param y_percent: the y axis value (forwards/backwards)
        :param x_percent: the x axis value (left/right)
        """
        self.drive.arcadeDrive(y_percent, x_percent)

    def update_gyro_pid(self):
        """This function updates the gyro PID values based on the error"""
        error = -self.get_gyro_angle()
        self.turn_power = self.KP * error

    def distance_to_ticks(self, distance_in_cm):
        """
        This function turns a given distance in cm into encoder ticks for the
        robot drive.
        :param distance_in_cm: the distance in cm to turn into encoder ticks
        :return: the same distance converted to encoder ticks
        """
        return distance_in_cm / self.DIST_TO_TICKS

    def reset_encoder(self):
        """This function resets the robot encoder"""
        self.encoding_motor.setQuadraturePosition(0, self.TIMEOUT_MS)

    def reset_gyro(self):
        """This function resets the robot gyro"""
        self.gyro.reset()

    def get_gyro_angle(self):
        """This function returns the gyro angle."""
        return self.gyro.getAngle()

    def returnPIDInput(self):
        """This function returns the input for the PID (encoder position)"""
        return self.encoding_motor.getQuadraturePosition()

    def usePIDOutput(self, output):
        """This function uses the PID output to drive the robot"""

        self.drive_robot(output, self.turn_power)
