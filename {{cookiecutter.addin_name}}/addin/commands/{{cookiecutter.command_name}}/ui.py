from enum import auto

import adsk.core, adsk.fusion

from ...libs.fusion_addin_framework import fusion_addin_framework as faf


class InputIds(faf.utils.InputIdsBase):
    Group1 = auto()
    Button1 = auto()


class InputsWindow:
    def __init__(self, command):
        self._command = command

        self._create_group_1()

    def _create_group_1(self):
        self.controls_group = self._command.commandInputs.addGroupCommandInput(
            InputIds.Group1.value, "Group1"
        )

        self.button_1 = self.controls_group.children.addBoolValueInput(
            InputIds.Button1.value, "Button 1", True
        )
