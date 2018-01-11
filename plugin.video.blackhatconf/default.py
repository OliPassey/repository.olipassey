# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Black Hat Conference
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
BASE3 = "plugin://plugin.video.youtube/play/?video_id="

YOUTUBE_CHANNEL_ID_1 = "PLH15HpR5qRsXtpLirwYHPWyqcEFPbr-uB"
YOUTUBE_CHANNEL_ID_2 = "PLH15HpR5qRsUyGhBVRDKGrHyQC5G4jQyd"
YOUTUBE_CHANNEL_ID_3 = "PLH15HpR5qRsWx4qw9ZlgmisHOcKG4ZcRS"


@route(mode='main_menu')
def Main_Menu():
	Add_Dir( 
		name="Black Hat Europe 2017", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
		icon="https://www.blackhat.com/images/page-graphics/metatag/event-logo-eu17.png")
	
	Add_Dir( 
		name="Black Hat USA 2017", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
		icon="https://www.blackhat.com/images/page-graphics/metatag/event-logo-us17.png")

	Add_Dir( 
		name="Black Hat Asia 2017", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
		icon="https://www.blackhat.com/images/page-graphics/metatag/event-logo-asia17.png")

		
@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()

@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)

if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))