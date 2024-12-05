import typing

import commands2
from subsystems.drivetrain import Drivetrain

class ArcadeDrive(commands2.CommandBase):
    def __init__(self,
                 arcade_drive: Drivetrain,
                 y: typing.Callable[[], float],
                 z: typing.Callable[[], float]
                 ) -> None:
        super().__init__()
        self.arcade_drive = arcade_drive
        self.y = y
        self.z = z
        self.addRequirements(arcade_drive)

    def execute(self) -> None:
        self.arcade_drive.arcade_drive(self.y(), self.z())

    def isFinished(self) -> bool: # pylint: disable=invalid-name
        return False

    def end(self) -> None:
        self.arcade_drive.arcade_drive(0, 0)
