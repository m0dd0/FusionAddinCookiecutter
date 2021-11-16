import logging
from uuid import uuid4
import traceback

import adsk.core, adsk.fusion, adsk.cam

from .fusion_addin_framework import fusion_addin_framework as faf

# settings / constants
LOGGING_ENABLED = True

# globals
addin = None

def on_created(event_args: adsk.core.CommandCreatedEventArgs):
    command = event_args.command

    
def on_execute(event_args: adsk.core.CommandEventArgs):
    pass

def on_input_changed(event_args: adsk.core.InputChangedEventArgs):
    # inputs = event_args.inputs # !!! do NOT use this because of bug
    # (will only contain inputs of the same input group)
    inputs = event_args.firingEvent.sender.commandInputs


def on_key_down(event_args: adsk.core.KeyboardEventArgs):
    pass

def on_destroy(event_args: adsk.core.CommandEventArgs):
    pass

### ENTRY POINT ###
def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        if LOGGING_ENABLED:
            faf.utils.create_logger(
                faf.__name__,
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
            resourceFolder="lightbulb",
            name="ADDIN_NAME",
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
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        addin.stop()
    except:
        msg = "Failed:\n{}".format(traceback.format_exc())
        if ui:
            ui.messageBox(msg)
        print(msg)