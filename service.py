import time
import os
import xbmc
import xbmcgui

dialog = xbmcgui.Dialog()
override = False
camera1 = "127.0.0.1"
# Camera2 = "127.6.5.4" Not used yet


def StartStream():
    xbmc.executebuiltin("PlayMedia(~/PycharmProjects/XBMC-Camera/Test.strm)")
    dialog.notification('Race Cam', 'Starting', xbmcgui.NOTIFICATION_INFO, 5000)
    return


def CamPing(camera):
    response = os.system("ping -c 1 " + camera)
    if response == 0:
        return True
    else:
        return False


class StreamPlayer(xbmc.Player):
    def __init__(self):
        xbmc.Player.__init__(self)


if not override:
    StartStream()