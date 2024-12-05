import commands2
import commands2.button

import wpilib

import constants

from subsystems.drivetrain import Drivetrain
from subsystems.limelight import LimelightSystem

from commands.arcadedrive import ArcadeDrive
from commands.limelightdisplay import LimelightDisplay
from commands.driveforward import DriveForward

class RobotContainer:
    def __init__(self) -> None:
        self.limelight = LimelightSystem()
        self.drivetrain = Drivetrain()
        self.stick = wpilib.Joystick(constants.DRIVE_JOYSTICK_PORT)
        self.configure_button_bindings()
        self.autonomous_command = DriveForward(self.drivetrain, self.limelight)

    def configure_button_bindings(self) -> None:
        combined = commands2.ParallelCommandGroup(
            ArcadeDrive(self.drivetrain, lambda: self.stick.getX(), lambda: self.stick.getY()), # pylint: disable=unnecessary-lambda
            LimelightDisplay(self.limelight)
        )
        self.drivetrain.setDefaultCommand(combined)

    def get_autonomous_command(self) -> commands2.Command:
        return self.autonomous_command
