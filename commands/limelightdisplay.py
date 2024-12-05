import commands2
from subsystems.limelight import LimelightSystem

class LimelightDisplay(commands2.CommandBase):
    def __init__(self, limelight: LimelightSystem) -> None:
        super().__init__()
        self.limelight = limelight
        self.addRequirements(limelight)

    def execute(self) -> None:
        results = self.limelight.get_results()
        print(results.tag_id if results else 'none')

    def isFinished(self) -> bool: # pylint: disable=invalid-name
        return False

    def end(self) -> None:
        pass
