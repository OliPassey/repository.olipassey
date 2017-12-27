# -*- coding: utf-8 -*-

# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: DEF CON Talks
# Author: Oli Passey (DoubleT)

#----------------------------------------------------------------

import os           
import xbmc         
import xbmcaddon    
import xbmcplugin   

from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File

debug        = Addon_Setting(setting='debug')       # Grab the setting of our debug mode in add-on settings
addon_id     = xbmcaddon.Addon().getAddonInfo('id') # Grab our add-on id

# Set the base plugin url you want to hook into
BASE  = "plugin://plugin.video.youtube/playlist/"
BASE2 = "plugin://plugin.video.youtube/channel/"

# Set each of your YouTube playlist id's
YOUTUBE_CHANNEL_ID_1 = "PL9fPq3eQfaaDOo8mTBHhEHMfuG2LNUSTC"
YOUTUBE_CHANNEL_ID_2 = "PL9fPq3eQfaaBCdjbKFYjosh1s1EkaYdsQ"
YOUTUBE_CHANNEL_ID_3 = "PL9fPq3eQfaaBuHqVvDzPoWxznYYmyx5UX"
YOUTUBE_CHANNEL_ID_4 = "PL9fPq3eQfaaAvXV3hJc4yHuNxoviVckoE"
YOUTUBE_CHANNEL_ID_5 = "UCur4HQg-2EQltweoKQfwOfg"
YOUTUBE_CHANNEL_ID_6 = "PL9fPq3eQfaaBD_8E9PJ8yyiTL0JhynlGK"
YOUTUBE_CHANNEL_ID_7 = "PL9fPq3eQfaaCIZajWLyN5f6M0HoU_Avuk"
YOUTUBE_CHANNEL_ID_8 = "PL9fPq3eQfaaDcbIEMSzdL5yuzh_m6BB-E"

@route(mode='main_menu')
def Main_Menu():
    Add_Dir( 
        name="DEF CON 25 (2017)", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="https://www.defcon.org/images/defcon-25/post-images/dc-25-logo.jpg")

    Add_Dir( 
        name="DEF CON 24 (2016)", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="https://www.defcon.org/images/defcon-24/dc-24-logo-sm.png")

    Add_Dir( 
        name="DEF CON 23 (2015)", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="https://www.defcon.org/images/defcon-23/dc-23-logo-sm.jpg")

    Add_Dir( 
        name="DEF CON 22 (2014)", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="https://www.defcon.org/images/defcon-22/dc-22-web.jpg")

    Add_Dir( 
        name="DEF CON 21 (2013)", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="https://www.defcon.org/images/defcon-21/dc-21-logo-sm.png")

    Add_Dir( 
        name="DEF CON 20 (2012)", url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="https://www.defcon.org/images/defcon-20/dc20-logo_smsq.png")
		
    Add_Dir( 
        name="DEF CON 20 Documentary", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="https://www.defcon.org/images/defcon-20/dc20-logo_smsq.png")		

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