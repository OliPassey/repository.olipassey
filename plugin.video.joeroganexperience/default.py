# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: joeroganexperience
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

YOUTUBE_CHANNEL_ID_1 = "PLk1Sqn_f33KvtMA4mCQSnzGsZe8qsTdzV"
YOUTUBE_CHANNEL_ID_2 = "PLk1Sqn_f33KtUuWHwNl3ndvbPKlQ6LJZB"
YOUTUBE_CHANNEL_ID_3 = "PLk1Sqn_f33Kvv8T6ZESpJ2nvEHT9xBhlb"
YOUTUBE_CHANNEL_ID_4 = "PLk1Sqn_f33KtVQWWnE_V6-sypm5zUMkU6"
YOUTUBE_CHANNEL_ID_5 = "PLk1Sqn_f33KuU_aJDvMPPAy_SoxXTt_ub"
YOUTUBE_CHANNEL_ID_6 = "PLk1Sqn_f33Ku0Oa3t8MQjV7D_G_PBi8g1"
YOUTUBE_CHANNEL_ID_7 = "PLk1Sqn_f33KtkaiY3M2r1LKmW3vB7UfE1"
YOUTUBE_CHANNEL_ID_8 = "PLk1Sqn_f33KtA0OOlTxl7CHizKmKeD70T"
YOUTUBE_CHANNEL_ID_9 = "PLk1Sqn_f33KuQyLE4RjEOdJ_-0epbcBb4"
YOUTUBE_CHANNEL_ID_10 = "PLk1Sqn_f33KuS7ZSVMJqzFaqOyyl-esmG"

@route(mode='main_menu')
def Main_Menu():
    Add_Dir(
        name="Latest Joe Rogram Experience", url=BASE+YOUTUBE_CHANNEL_ID_10+"/", folder=True,
        icon="https://yt3.ggpht.com/a-/AN66SAyJWj4wg2agMY20Ma5mrECrCy6m1nxzwuRO1w=s900-mo-c-c0xffffffff-rj-k-no")

    Add_Dir(
        name="JRE Archive #1001 - Current", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="https://yt3.ggpht.com/a-/AN66SAyJWj4wg2agMY20Ma5mrECrCy6m1nxzwuRO1w=s900-mo-c-c0xffffffff-rj-k-no")

    Add_Dir(
        name="JRE Archive #701 - 1000", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="https://yt3.ggpht.com/a-/AN66SAyJWj4wg2agMY20Ma5mrECrCy6m1nxzwuRO1w=s900-mo-c-c0xffffffff-rj-k-no")

    Add_Dir(
        name="JRE Archive #500 - 700", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="https://yt3.ggpht.com/a-/AN66SAyJWj4wg2agMY20Ma5mrECrCy6m1nxzwuRO1w=s900-mo-c-c0xffffffff-rj-k-no")

    Add_Dir(
        name="JRE Archive #350 - 499", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="https://yt3.ggpht.com/a-/AN66SAyJWj4wg2agMY20Ma5mrECrCy6m1nxzwuRO1w=s900-mo-c-c0xffffffff-rj-k-no")

    Add_Dir(
        name="JRE Archive #200 - 349", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="https://yt3.ggpht.com/a-/AN66SAyJWj4wg2agMY20Ma5mrECrCy6m1nxzwuRO1w=s900-mo-c-c0xffffffff-rj-k-no")

    Add_Dir(
        name="JRE Archive #1 - 199", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="https://yt3.ggpht.com/a-/AN66SAyJWj4wg2agMY20Ma5mrECrCy6m1nxzwuRO1w=s900-mo-c-c0xffffffff-rj-k-no")

@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()

@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)

if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
