import commands2
import wpilib.drive

from subsystems.drivetrain import Drivetrain
from subsystems.limelight import limelightSystem

class DriveForward(commands2.CommandBase):
    def __init__(self, drivetrain: Drivetrain, limelight: limelightSystem) -> None:
        super().__init__()
        self.drivetrain = drivetrain
        self.limelight = limelight
        self.addRequirements(drivetrain, limelight)

    def initialize(self) -> None:
        self.timer = wpilib.Timer()
        self.timer.start()

    def execute(self) -> None:
        results = self.limelight.get_results()

        tag = results.tagId if results else -1

        print(tag)

        if tag == 1:
            # Forward
            self.drivetrain.arcadeDrive(0, 0.5)
        elif tag == 2:

            # Left
            self.drivetrain.arcadeDrive(0.5, 0)
        elif tag == 3:

            # Right
            self.drivetrain.arcadeDrive(-0.5, 0)
        elif tag == 4:

            # Backward
            self.drivetrain.arcadeDrive(0, -0.5)

    def isFinished(self) -> bool:
        return False

    def end(self) -> None:
        self.drivetrain.arcadeDrive(0, 0)