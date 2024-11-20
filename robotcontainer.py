import constants

import commands2
import commands2.button

import wpilib

from subsystems.drivetrain import Drivetrain
from commands.arcadedrive import ArcadeDrive

from subsystems.limelight import limelightSystem
from commands.limelightdisplay import limelightDisplay
from commands.driveforward import DriveForward

class RobotContainer:
    def __init__(self) -> None:
        self.limelight = limelightSystem()
        self.drivetrain = Drivetrain()
        self.stick = wpilib.Joystick(constants.DRIVE_JOYSTICK_PORT)
        self.configureButtonBindings()
        self.autonomousCommand = DriveForward(self.drivetrain, self.limelight)

    def configureButtonBindings(self) -> None:
        combined = commands2.ParallelCommandGroup(
            ArcadeDrive(self.drivetrain, lambda: self.stick.getX(), lambda: self.stick.getY()),
            limelightDisplay(self.limelight)
        )
        self.drivetrain.setDefaultCommand(combined)

    def getAutonomousCommand(self) -> commands2.Command:
        return self.autonomousCommand