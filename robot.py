#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#
import typing

import commands2

from robotcontainer import RobotContainer

class MyRobot(commands2.TimedCommandRobot):
    """
    This is a demo program showing the use of the DifferentialDrive class.
    Runs the motors with arcade steering.
    """

    autonomous_command: typing.Optional[commands2.Command] = None

    def robotInit(self) -> None:
        """Robot initialization function"""
        self.container = RobotContainer()

    def autonomousInit(self) -> None:
        """Called when autonomous mode is enabled"""
        self.autonomous_command = self.container.get_autonomous_command()

        if self.autonomous_command:
            self.autonomous_command.schedule()

    def teleopPeriodic(self) -> None:
        commands2.CommandScheduler.getInstance().run()
