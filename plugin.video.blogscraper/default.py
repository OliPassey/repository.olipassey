# -*- coding: utf-8 -*-

#----------------------------------------------------------------

# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: olipassey.me.uk vidscraper
# Author: Oli Passey (DoubleT)

#----------------------------------------------------------------

import os           
import xbmc         
import xbmcaddon    
import xbmcplugin

from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File

#------------------------------------------------------------

debug        = Addon_Setting(setting='debug')       # Grab the setting of our debug mode in add-on settings
addon_id     = xbmcaddon.Addon().getAddonInfo('id') # Grab our add-on id

# Set the base plugin url you want to hook into
BASE  = "plugin://plugin.video.youtube/playlist/"
BASE2 = "plugin://plugin.video.youtube/channel/"

# Set each of your YouTube playlist id's
YOUTUBE_CHANNEL_ID_1 = "PL9fPq3eQfaaDOo8mTBHhEHMfuG2LNUSTC"
YOUTUBE_CHANNEL_ID_2 = "PLTibR1K5pEHgBoz2y8Guytjry8m-4nwcd"
YOUTUBE_CHANNEL_ID_3 = "PLC474234E124B5213"
YOUTUBE_CHANNEL_ID_4 = "PL9fPq3eQfaaAvXV3hJc4yHuNxoviVckoE"
YOUTUBE_CHANNEL_ID_5 = "UCur4HQg-2EQltweoKQfwOfg"


@route(mode='main_menu')
def Main_Menu():

    Add_Dir( 
        name="DEF CON 25 (2017)", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="https://i2.wp.com/itmeets.guru/wp-content/uploads/2017/05/Untitled-design-2.jpg?resize=642%2C360&ssl=1")

    Add_Dir( 
        name="DEF CON 24 (2016)", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="https://www.defcon.org/images/defcon-24/dc-24-logo-sm.png")

    Add_Dir( 
        name="SpaceX: Launches", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="http://outerbusiness.com/wp-content/uploads/2015/09/spacex.jpg")

    Add_Dir( 
        name="Oli's YouTube Channel", url=BASE2+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="http://mediad.publicbroadcasting.net/p/wcbu/files/styles/medium/public/201610/YouTube-logo.png")
#----------------------------------------------------------------
# A basic OK Dialog
@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()
#----------------------------------------------------------------
# A basic OK Dialog
@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)
#----------------------------------------------------------------

if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))