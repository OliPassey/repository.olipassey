# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Friends of the Earth - England, Wales & Northern Ireland
# Author: Oli Passey (DoubleT)
# This plugins is technically capable of playing YouTube Videos, Playlists & Channels
# Vimeo functionality is limited to search terms & individual videos. 
# Channels, Users or Playlists are not supported at this time
#----------------------------------------------------------------

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
BASE3 = "plugin://plugin.video.vimeo/kodion/search/query/?q=/"
BASE4 = "plugin://plugin.video.vimeo/play/?video_id="
BASE5 = "plugin://plugin.video.youtube/play/?video_id="

VIDEO_CHANNEL_ID_1 = "wwwfoecouk"
VIDEO_CHANNEL_ID_2 = "PLBg4Y5CtDgq4AoWO4OHEaZt8nNaAyFOt-"
VIDEO_CHANNEL_ID_3 = "230151586"
VIDEO_CHANNEL_ID_4 = "PL9fPq3eQfaaAvXV3hJc4yHuNxoviVckoE"
VIDEO_CHANNEL_ID_5 = "UCur4HQg-2EQltweoKQfwOfg"
VIDEO_CHANNEL_ID_6 = "PL9fPq3eQfaaBD_8E9PJ8yyiTL0JhynlGK"
VIDEO_CHANNEL_ID_7 = "PL9fPq3eQfaaCIZajWLyN5f6M0HoU_Avuk"
VIDEO_CHANNEL_ID_8 = "PL9fPq3eQfaaDcbIEMSzdL5yuzh_m6BB-E"
VIDEO_CHANNEL_ID_9 = "PL9fPq3eQfaaDcbIEMSzdL5yuzh_m6BB-E"

@route(mode='main_menu')
def Main_Menu():
    Add_Dir( 
        name="Our latest videos", url=BASE3+VIDEO_CHANNEL_ID_1, folder=True,
        icon="https://cdn.friendsoftheearth.uk/themes/custom/foed8/logo.png",
        fanart="https://static.pexels.com/photos/240040/pexels-photo-240040.jpeg",
        description="Our latest social media videos")
            
    Add_Dir( 
        name="Save the bees", url=BASE+VIDEO_CHANNEL_ID_2+"/", folder=True,
        icon="https://cdn.friendsoftheearth.uk/sites/default/files/styles/link_collection/public/media/images/Bee%20on%20lavender.jpg",
        fanart="http://www.foeeurope.org/sites/default/files/theflood-7710_0.jpg",
        description="Join the generation that save the bees")

    Add_Dir( 
        name="Fight air pollution", url=BASE4+VIDEO_CHANNEL_ID_3+"/",
        icon="https://cdn.friendsoftheearth.uk/sites/default/files/styles/link_collection/public/Emi_001.jpg",
        fanart="http://www.foeeurope.org/sites/default/files/theflood-7710_0.jpg")

    Add_Dir( 
        name="Save the climate, stop fracking", url=BASE3+VIDEO_CHANNEL_ID_1, folder=True,
        icon="https://cdn.friendsoftheearth.uk/sites/default/files/styles/link_collection/public/media/images/fracking%20win%20preston.jpg",
        fanart="https://i.vimeocdn.com/portrait/19833009_300x300.webp")
    
    Add_Dir( 
        name="Defend EU nature laws", url=BASE3+VIDEO_CHANNEL_ID_1, folder=True,
        icon="https://cdn.friendsoftheearth.uk/sites/default/files/styles/link_collection/public/media/images/RS21342_iStock_000017244388_Large-scr.jpg",
        fanart="https://i.vimeocdn.com/portrait/19833009_300x300.webp")
    
    Add_Dir( 
        name="Keep dirty energy in the ground", url=BASE3+VIDEO_CHANNEL_ID_1, folder=True,
        icon="https://cdn.friendsoftheearth.uk/sites/default/files/styles/link_collection/public/media/images/climate-refugees-Papa-New-Guinea_0.jpg",
        fanart="https://i.vimeocdn.com/portrait/19833009_300x300.webp")

    Add_Dir( 
        name="Help nature", url=BASE3+VIDEO_CHANNEL_ID_1, folder=True,
        icon="https://cdn.friendsoftheearth.uk/sites/default/files/styles/link_collection/public/dfkt-120820.jpg",
        fanart="https://i.vimeocdn.com/portrait/19833009_300x300.webp")

    Add_Dir( 
        name="Eat well", url=BASE3+VIDEO_CHANNEL_ID_1, folder=True,
        icon="https://cdn.friendsoftheearth.uk/sites/default/files/styles/link_collection/public/media/images/vegetarian%20meal%20preparation.jpg",
        fanart="https://i.vimeocdn.com/portrait/19833009_300x300.webp")

    Add_Dir( 
        name="Use less stuff", url=BASE3+VIDEO_CHANNEL_ID_1, folder=True,
        icon="https://cdn.friendsoftheearth.uk/sites/default/files/styles/link_collection/public/media/images/junk-shop.jpg",
        fanart="https://i.vimeocdn.com/portrait/19833009_300x300.webp")

@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()

@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)


if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))