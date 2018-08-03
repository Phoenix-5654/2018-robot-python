import math

import wpilib
import wpilib.drive
from wpilib.command import PIDSubsystem


class Drivetrain(PIDSubsystem):
    WHL_DIAMETER = 15.24
    WHL_CIRC = WHL_DIAMETER * math.pi

    ENCODER_RES = 1024

    DIST_TO_TICKS = WHL_CIRC / ENCODER_RES

    QUAD_MULTIPLIER = 4

    STRENGTH_GEAR_RATIO = 16.5

    SPD_STATE = 1
    STR_STATE = 2

    TIMEOUT_MS = 30

    MAX_SPEED = 0.4
    MIN_SPEED = -MAX_SPEED

    KP = 0.067

    def __init__(self, left, right, solenoid, gyro, encoding_motor):
        super().__init__(0.001, 0, 0, name='Drivetrain')

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
        self.solenoid.set(self.SPD_STATE)

    def strength_state(self):
        self.solenoid.set(self.STR_STATE)

    def state(self):

        return self.solenoid.get()

    def drive_robot(self, y_percent, x_percent):
        self.drive.arcadeDrive(y_percent, x_percent)

    def update_gyro_pid(self):
        error = -self.gyro.getAngle()
        self.turn_power = self.KP * error

    def distance_to_ticks(self, distance_in_cm):
        return distance_in_cm / self.DIST_TO_TICKS * self.QUAD_MULTIPLIER * \
               self.STRENGTH_GEAR_RATIO

    def reset_encoder(self):
        self.encoding_motor.setQuadraturePosition(0, self.TIMEOUT_MS)

    def reset_gyro(self):
        self.gyro.reset()

    def get_gyro_angle(self):
        return self.gyro.getAngle()

    def returnPIDInput(self):
        return self.encoding_motor.getQuadraturePosition()

    def usePIDOutput(self, output):
        print("Output:", output)

        self.drive_robot(output, self.turn_power)
