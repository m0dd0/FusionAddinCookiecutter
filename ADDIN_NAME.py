import logging
from uuid import uuid4
import traceback

import adsk.core, adsk.fusion, adsk.cam

from .fusion_addin_framework import fusion_addin_framework as faf

LOGGING_ENABLED = True

addin = None

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
        mover_event_id = str(uuid4())
        cmd = faf.AddinCommand(
            control,
            resourceFolder="gear",
            name="Snacade",
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