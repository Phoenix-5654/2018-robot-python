import ctre
import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Command, Scheduler

import oi
from commands.autonomous import AutonomousProgram
from commands.followjoystick import FollowJoystick
from subsystems import drivetrain, elevator, grippers, handles


class MyRobot(CommandBasedRobot):

    def robotInit(self):
        Command.getRobot = lambda _: self

        wpilib.CameraServer.launch()

        self.joystick = wpilib.Joystick(0)

        self.lr_motor = ctre.WPI_TalonSRX(1)
        self.lf_motor = ctre.WPI_TalonSRX(2)

        self.rr_motor = ctre.WPI_TalonSRX(5)
        self.rf_motor = ctre.WPI_TalonSRX(6)

        self.left = wpilib.SpeedControllerGroup(self.lf_motor, self.lr_motor)
        self.right = wpilib.SpeedControllerGroup(self.rf_motor, self.rr_motor)

        self.drivetrain_solenoid = wpilib.DoubleSolenoid(2, 3)

        self.drivetrain_gyro = wpilib.AnalogGyro(1)

        self.drivetrain = drivetrain.Drivetrain(self.left, self.right,
                                                self.drivetrain_solenoid,
                                                self.drivetrain_gyro,
                                                self.rf_motor)

        self.l_gripper = wpilib.VictorSP(0)
        self.r_gripper = wpilib.VictorSP(1)

        self.grippers = grippers.Grippers(self.l_gripper, self.r_gripper)

        self.elevator_motor = wpilib.VictorSP(2)
        self.elevator_top_switch = wpilib.DigitalInput(4)
        self.elevator_bot_switch = wpilib.DigitalInput(5)

        self.elevator = elevator.Elevator(self.elevator_motor,
                                          self.elevator_top_switch,
                                          self.elevator_bot_switch)

        self.handles_solenoid = wpilib.DoubleSolenoid(0, 1)

        self.handles = handles.Handles(self.handles_solenoid)

        self.autonomous = AutonomousProgram()

        self.josytick = oi.getJoystick()

    def autonomousInit(self):
        self.autonomous.start()

        Scheduler.getInstance().run()

    def teleopInit(self):
        self.drivetrain.setDefaultCommand(FollowJoystick())

if __name__ == '__main__':
    wpilib.run(MyRobot, physics_enabled=True)
