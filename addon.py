import xbmcaddon
import xbmcgui
import xbmcvfs



addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

line2 = xbmc.getInfoLabel("Player.Filenameandpath")
line1 = "Delete file"
line3 = ""

answer = xbmcgui.Dialog().yesno("Delete", line1, line2, line3, "No", "Yes")


def moveToNext():
    xbmc.executebuiltin('PlayerControl(next)')
    # xbmc.executebuiltin('Action(ACTION_PLAYER_FORWARD)')
    # xbmc.Player().playnext()


def deleteFile():
    ret = xbmcvfs.delete(line2)

    if ret:
        msg = "File deleted successful"
        icon = xbmcgui.NOTIFICATION_INFO
    else:
        msg = "File didn't deleted"
        icon = xbmcgui.NOTIFICATION_ERROR

    xbmcgui.Dialog().notification("Delete", msg, icon, 1000)


if answer:
    deleteFile()
    moveToNext()
