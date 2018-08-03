from wpilib.buttons.joystickbutton import JoystickButton
from wpilib.joystick import Joystick

from commands.drivetrainstate import DrivetrainState
from commands.elevatordown import ElevatorDown
from commands.elevatorup import ElevatorUp
from commands.exhaust import GrippersExhaust
from commands.handlesclose import HandlesClose
from commands.handlesopen import HandlesOpen
from commands.handlesstate import HandlesState
from commands.intake import GrippersIntake
from commands.speedstate import SpeedState
from commands.strengthstate import StrengthState
from triggers.pov import POVButton


def getJoystick():

    joystick = Joystick(0)

    trigger = JoystickButton(joystick, Joystick.ButtonType.kTrigger)
    trigger.whileHeld(GrippersIntake())

    thumb = JoystickButton(joystick, Joystick.ButtonType.kTop)
    thumb.whileHeld(GrippersExhaust())

    POV_up = POVButton(joystick, 0)
    POV_down = POVButton(joystick, 180)

    POV_up.whileActive(ElevatorUp())
    POV_down.whileActive(ElevatorDown())

    button_5 = JoystickButton(joystick, 5)
    button_5.whenPressed(HandlesState(HandlesOpen(), HandlesClose()))

    button_6 = JoystickButton(joystick, 6)
    button_6.whenPressed(DrivetrainState(StrengthState(), SpeedState()))

    return joystick
