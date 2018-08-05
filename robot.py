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
        """This function initiates the robot's components and parts"""

        # Here we create a function for the command class to return the robot
        # instance, so that we don't have to import the robot module for each
        # command.
        Command.getRobot = lambda _: self

        # This launches the camera server between the robot and the computer
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

        # Here we create the drivetrain as a whole, combining all the different
        # robot drivetrain compontents.
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

        # This creates the instance of the autonomous program that will run
        # once the autonomous period begins.
        self.autonomous = AutonomousProgram()

        # This gets the instance of the joystick with the button function
        # programmed in.
        self.josytick = oi.getJoystick()

    def autonomousInit(self):
        """This function operates at the beginning of the autonomous period"""
        self.autonomous.start()

        # We run the scheduler to fix thread issues that might occur
        Scheduler.getInstance().run()

    def teleopInit(self):
        """This function runs at the beginning of the teleop period"""

        # Here we set the drivetrain's default command to FollowJoystick().
        # Meaning that once the teleop begins, the robot will be controlled by
        # the joystick.
        self.drivetrain.setDefaultCommand(FollowJoystick())


if __name__ == '__main__':
    wpilib.run(MyRobot, physics_enabled=True)
