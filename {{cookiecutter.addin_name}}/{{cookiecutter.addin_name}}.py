import logging
import traceback
from pathlib import Path

import adsk.core, adsk.fusion

import adsk.core, adsk.fusion

from .{{cookiecutter.addin_name}}.fusion_addin_framework import fusion_addin_framework as faf

from .{{cookiecutter.addin_name}}.logic_model import *
from .{{cookiecutter.addin_name}}.ui import CommandWindow, InputIds


# settings / constants #########################################################
LOGGING_ENABLED = True
RESOURCE_FOLDER = (
    Path(__file__).parent
    / "{{cookiecutter.addin_name}}"
    / "fusion_addin_framework"
    / "fusion_addin_framework"
    / "default_images"
)
# RESOURCE_FOLDER = Path(__file__).parent / "resources"

# region
# standard, declarative approach
# globals ######################################################################
addin = None
ao = faf.utils.AppObjects()


# handlers #####################################################################
def on_created(event_args: adsk.core.CommandCreatedEventArgs):
    command = event_args.command
    command_window = CommandWindow(command, RESOURCE_FOLDER)


def on_execute(event_args: adsk.core.CommandEventArgs):
    pass


def on_input_changed(event_args: adsk.core.InputChangedEventArgs):
    # do NOT use this: inputs = event_args.inputs
    # (will only contain changed inputs of the same input group)
    # use instead: inputs = event_args.firingEvent.sender.commandInputs

    if event_args.input.id == InputIds.Button1.value:
        ao.userInterface.messageBox("Button clicked.")


def on_destroy(event_args: adsk.core.CommandEventArgs):
    pass


### entry point ################################################################
def run(context):
    try:
        ui = ao.userInterface

        if LOGGING_ENABLED:
            faf.utils.create_logger(
                __name__,  # also applies to faf since its a submodule
                [logging.StreamHandler(), faf.utils.TextPaletteLoggingHandler()],
            )

        global addin
        addin = faf.FusionAddin()
        workspace = faf.Workspace(addin, id="FusionSolidEnvironment")
        tab = faf.Tab(workspace, id="ToolsTab")
        panel = faf.Panel(tab, id="SolidScriptsAddinsPanel")
        control = faf.Control(panel)

        cmd = faf.AddinCommand(
            control,
            resourceFolder="{{cookiecutter.control_image}}",
            name="{{cookiecutter.addin_name}}",
            commandCreated=on_created,
            inputChanged=on_input_changed,
            execute=on_execute,
            destroy=on_destroy,
        )

    except:
        msg = "Failed:\n{}".format(traceback.format_exc())
        if ui:
            ui.messageBox(msg)
        print(msg)


def stop(context):
    try:
        ui = ao.userInterface
        addin.stop()
    except:
        msg = "Failed:\n{}".format(traceback.format_exc())
        if ui:
            ui.messageBox(msg)
        print(msg)


# endregion

# region
# command cubclass approach
class MyCommand(faf.AddinCommand):
    def __init__(self):
        self.ao = faf.utils.AppObjects()

        addin = faf.FusionAddin()
        workspace = faf.Workspace(addin, id="FusionSolidEnvironment")
        tab = faf.Tab(workspace, id="ToolsTab")
        panel = faf.Panel(tab, id="SolidScriptsAddinsPanel")
        control = faf.Control(panel)

        super().__init__(
            control,
            resourceFolder="{{cookiecutter.control_image}}",
            name="{{cookiecutter.addin_name}}"
        )

    def on_execute(self, event_args):
        pass

    def on

        # if LOGGING_ENABLED:
        #     faf.utils.create_logger(
        #         __name__,  # also applies to faf since its a submodule
        #         [logging.StreamHandler(), faf.utils.TextPaletteLoggingHandler()],
        #     )


# endregion
