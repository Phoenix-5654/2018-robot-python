import ctre
import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Command

import oi
from subsystems import drivetrain, elevator, grippers, handles


class MyRobot(CommandBasedRobot):

    def robotInit(self):

        Command.getRobot = lambda _: self

        self.joystick = wpilib.Joystick(0)

        self.lr_motor = ctre.WPI_TalonSRX(1)
        self.lf_motor = ctre.WPI_TalonSRX(2)

        self.rr_motor = ctre.WPI_TalonSRX(5)
        self.rf_motor = ctre.WPI_TalonSRX(6)

        self.left = wpilib.SpeedControllerGroup(self.lf_motor, self.lr_motor)
        self.right = wpilib.SpeedControllerGroup(self.rf_motor, self.rr_motor)

        self.drivetrain_solenoid = wpilib.DoubleSolenoid(2, 3)

        self.drivetrain = drivetrain.Drivetrain(self.left, self.right,
                                                self.drivetrain_solenoid)

        self.l_gripper = wpilib.PWMVictorSPX(0)
        self.r_gripper = wpilib.PWMVictorSPX(1)

        self.grippers = grippers.Grippers(self.l_gripper, self.r_gripper)

        self.elevator_motor = wpilib.PWMVictorSPX(2)
        self.elevator_top_switch = wpilib.DigitalInput(4)
        self.elevator_bot_switch = wpilib.DigitalInput(5)

        self.elevator = elevator.Elevator(self.elevator_motor,
                                          self.elevator_top_switch,
                                          self.elevator_bot_switch)

        self.handles_solenoid = wpilib.DoubleSolenoid(0, 1)

        self.handles = handles.Handles(self.handles_solenoid)

        self.josytick = oi.getJoystick()


if __name__ == '__main__':
    wpilib.run(MyRobot, physics_enabled=True)
