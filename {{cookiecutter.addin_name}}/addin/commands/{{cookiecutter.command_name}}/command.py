import adsk.core, adsk.fusion  # pylint:disable=import-error

from ...libs.fusion_addin_framework import fusion_addin_framework as faf
from ... import config
from .ui import CommandWindow, InputIds
from .logic_model import {{cookiecutter.command_name}}Model


class {{cookiecutter.command_name}}Command(faf.AddinCommandBase):
    def __init__(self, addin: faf.FusionAddin):

        workspace = faf.Workspace(addin, id=config.{{cookiecutter.command_name.upper()}}_WORKSPACE_ID)
        tab = faf.Tab(workspace, id=config.{{cookiecutter.command_name.upper()}}_TAB_ID)
        panel = faf.Panel(tab, id=config.{{cookiecutter.command_name.upper()}}_PANEL_ID)
        control = faf.Control(panel)

        super().__init__(
            control,
            name=config.{{cookiecutter.command_name.upper()}}_COMMAND_NAME,
            tooltip=config.{{cookiecutter.command_name.upper()}}_TOOLTIP,
        )

        self.command_window = None
        self.model = None

    def commandCreated(self, eventArgs: adsk.core.CommandCreatedEventArgs):
        self.command_window = CommandWindow(eventArgs.command)
        self.model = {{cookiecutter.command_name}}Model(self.command_window)

    def inputChanged(self, eventArgs: adsk.core.InputChangedEventArgs):
        # do NOT use: inputs = event_args.inputs (will only contain inputs of the same input group as the changed input)
        # use instead: inputs = event_args.firingEvent.sender.commandInputs

        # if eventArgs.input.id == InputIds.<input_name>.value:
        #     pass

        pass

    def execute(
        self, eventArgs: adsk.core.CommandEventArgs  # pylint:disable=unused-argument
    ):
        pass

    def destroy(
        self, eventArgs: adsk.core.CommandEventArgs  # pylint:disable=unused-argument
    ):
        pass

