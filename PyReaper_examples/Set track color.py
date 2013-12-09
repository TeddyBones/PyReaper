from PyReaper import *

with undoable("Set track color to 'blue' if 'drum' in name"):
    """ All lines below are executed "inside" RPR_Undo_BeginBlock/RPR_RPR_Undo_EndBlock.
        "Set track color..." is the undo point name which can be seen f.ex. in the "undo history" view
        when this script is executed."""

    for track in get_all_tracks():
        if 'drum' in track.name:
            # color seems to be (B,G,R) not (R,G,B)
            track.color = (255,0,0)