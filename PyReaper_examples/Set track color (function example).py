from PyReaper import *

def setDrumTrackColorToBlue():
    for track in get_all_tracks():
        if 'drum' in track.name:
            # color seems to be (B,G,R) not (R,G,B)
            track.color = (255,0,0)

with undoable("Set track color to 'blue' if 'drum' in name"):
    """ Call setDrumTrackColorToBlue() inside RPR_Undo_BeginBlock/RPR_RPR_Undo_EndBlock."""
    setDrumTrackColorToBlue()

