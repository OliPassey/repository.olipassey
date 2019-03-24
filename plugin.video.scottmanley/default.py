# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: scottmanley
# Author: Oli Passey (DoubleT)


import os
import xbmc
import xbmcaddon
import xbmcplugin

from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File

debug        = Addon_Setting(setting='debug')
addon_id     = xbmcaddon.Addon().getAddonInfo('id')

BASE  = "plugin://plugin.video.youtube/playlist/"
BASE2 = "plugin://plugin.video.youtube/channel/"

YOUTUBE_CHANNEL_ID_1 = "UCxzC4EngIsMrPmbm6Nxvb-A"
YOUTUBE_CHANNEL_ID_2 = "PLYu7z3I8tdEmRqrGfi3eNIzHLa7ux1IMb"
YOUTUBE_CHANNEL_ID_3 = ""
YOUTUBE_CHANNEL_ID_4 = ""
YOUTUBE_CHANNEL_ID_5 = ""
YOUTUBE_CHANNEL_ID_6 = ""
YOUTUBE_CHANNEL_ID_7 = ""
YOUTUBE_CHANNEL_ID_8 = ""
YOUTUBE_CHANNEL_ID_9 = ""
YOUTUBE_CHANNEL_ID_10 = ""

@route(mode='main_menu')
def Main_Menu():
    Add_Dir(
        name="Latest Videos", url=BASE2+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="https://banner2.kisspng.com/20180331/gqw/kisspng-youtube-play-button-clip-art-youtube-logo-5abf62e1e59f11.1826685915224921299405.jpg")

    Add_Dir(
        name="Playlist - Human Spaceflight", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Wisoff_on_the_Arm_-_GPN-2000-001069.jpg/300px-Wisoff_on_the_Arm_-_GPN-2000-001069.jpg")
@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()

@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)

if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
