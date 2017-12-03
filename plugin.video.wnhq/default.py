import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)

if mode is None:
    url = build_url({'mode': 'folder', 'foldername': 'Folder One'})
    li = xbmcgui.ListItem('Live Radio (Audio)', iconImage='http://cdn.instructables.com/F21/3AKT/FX5571DH/F213AKTFX5571DH.MEDIUM.gif')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    url = build_url({'mode': 'folder6', 'foldername': 'Folder One'})
    li = xbmcgui.ListItem('YouTube Live Streams (Audio & Video)', iconImage='http://cdn.instructables.com/F21/3AKT/FX5571DH/F213AKTFX5571DH.MEDIUM.gif')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    url = build_url({'mode': 'folder1', 'foldername': 'Folder Two'})
    li = xbmcgui.ListItem('DJ Klass-A Radio Recordings', iconImage='http://static.house-mixes.com/s3/webmixes-images/accounts-410112/artwork/efa00ee9-1270-4820-92b3-0f502a85ced3.jpg/400/45/true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    url = build_url({'mode': 'folder2', 'foldername': 'Folder Two'})
    li = xbmcgui.ListItem('WhiteNoiseHQ Vs Ballistic Beats', iconImage='http://www.whitenoisehq.co.uk/v3/WN&BBFront.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    url = build_url({'mode': 'folder3', 'foldername': 'Folder Two'})
    li = xbmcgui.ListItem('WhiteNoiseHQ - The Freeform Special', iconImage='http://farm5.static.flickr.com/4089/5040817729_d7d6efcb8e_b.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    url = build_url({'mode': 'folder4', 'foldername': 'Folder Two'})
    li = xbmcgui.ListItem('Lady Brock - House Series', iconImage='http://static.house-mixes.com/s3/webmixes-images/accounts-88106/artwork/73c5708c-8276-4545-afd7-b367d8bc760d.jpg/360/45/true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    url = build_url({'mode': 'folder5', 'foldername': 'Folder Two'})
    li = xbmcgui.ListItem('White Noise HQ Recordings', iconImage='http://static.house-mixes.com/s3/webmixes-images/accounts-88106/artwork/73c5708c-8276-4545-afd7-b367d8bc760d.jpg/360/45/true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder':
    foldername = args['foldername'][0]
    url = 'http://whitenoisehq.co.uk/v3/RevoltLive.m3u'
    li = xbmcgui.ListItem('Revolt Party - Live Stream', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://whitenoisehq.co.uk/v3/RevoltBot.m3u'
    li = xbmcgui.ListItem('Revolt Party - AutoDJ', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://whitenoisehq.co.uk/v3/PLUR.pls'
    li = xbmcgui.ListItem('Peace Love Unity Radio', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    xbmcplugin.endOfDirectory(addon_handle)
	
elif mode[0] == 'folder1':
    foldername = args['foldername'][0]
    url = 'http://lnd1.house-mixes.com/m/klass-a/3c081bc2-4404-45f7-8d2a-88f92441d77b.mp3'
    li = xbmcgui.ListItem('DJ Klass-A - PLURadio 1st November 2014 (Hard House)', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://lnd1.house-mixes.com/m/klass-a/0db80df5-8568-4e87-9d44-20d4ec6ec77b.mp3'
    li = xbmcgui.ListItem('DJ Klass-A - PLURadio 25th October 2014 (UK Hardcore)', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://lnd1.house-mixes.com/m/klass-a/be09b7e3-989c-4a0d-a7a8-d494096091d7.mp3'
    li = xbmcgui.ListItem('DJ Klass-A with MC Tom Thumb - PLURadio 18th October 2014 (UK Hardcore)', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://lnd1.house-mixes.com/m/klass-a/f892c47f-e6d9-4e5a-800e-60c88854568a.mp3'
    li = xbmcgui.ListItem('DJ Klass-A - Revolt Party 19th October 2014 (UK Hardcore)', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://lnd1.house-mixes.com/m/klass-a/11f7b6a5-1c3a-4904-b7ae-77a6a2d91a89.mp3'
    li = xbmcgui.ListItem('DJ Klass-A - Revolt Party 12th October 2014 *(Gabba)', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder2':
    foldername = args['foldername'][0]
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=29'
    li = xbmcgui.ListItem('Lady Brock b2b Double T @ White Noise HQ Vs Ballistic Beatz', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=27'
    li = xbmcgui.ListItem('Klass A b2b Program @ White Noise HQ Vs Ballistic Beatz', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=28'
    li = xbmcgui.ListItem('Kurt @ White Noise HQ Vs Ballistic Beatz', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=24'
    li = xbmcgui.ListItem('Darwin @ White Noise HQ Vs Ballistic Beatz', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=26'
    li = xbmcgui.ListItem('JB-C b2b Clodhopper @ White Noise HQ Vs Ballistic Beatz', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=30'
    li = xbmcgui.ListItem('Lil Miss Detonate b2b Bernzey @ White Noise HQ Vs Ballistic Beatz', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=25'
    li = xbmcgui.ListItem('Hoodzie b2b Vapour @ White Noise HQ Vs Ballistic Beatz', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=32'
    li = xbmcgui.ListItem('Mizel @ White Noise HQ Vs Ballistic Beatz', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=31'
    li = xbmcgui.ListItem('Hoodzie b2b Distortion @ White Noise HQ Vs Ballistic Beatz', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder3':
    foldername = args['foldername'][0]
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=36'
    li = xbmcgui.ListItem('Kevin Energy @ White Noise HQ - The Freeform Special', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=39'
    li = xbmcgui.ListItem('Nick235 @ White Noise HQ - The Freeform Special', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=38'
    li = xbmcgui.ListItem('Lady Brock @ White Noise HQ - The Freeform Special', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=33'
    li = xbmcgui.ListItem('Solution @ White Noise HQ - The Freeform Special', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=35'
    li = xbmcgui.ListItem('Greg Peaks & Pinnacle @ White Noise HQ - The Freeform Special', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=37'
    li = xbmcgui.ListItem('Klass-A & Program @ White Noise HQ - The Freeform Special', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/?dl_id=34'
    li = xbmcgui.ListItem('Double T @ White Noise HQ - The Freeform Special', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder4':
    foldername = args['foldername'][0]
    url = 'http://lnd1.house-mixes.com/m/lady%20brock/dab511e3-c2ae-4418-b658-cb71ec528032.mp3'
    li = xbmcgui.ListItem('Lady Brock - House Series - 001 Tech & Progressive', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://lnd1.house-mixes.com/m/lady%20brock/54bac03a-a1dc-4e9f-8d37-95581a1c9792.mp3'
    li = xbmcgui.ListItem('Lady Brock - House Series - 002 Electro', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder5':
    foldername = args['foldername'][0]
    url = 'http://www.whitenoisehq.co.uk/v3/wnhq001.m3u'
    li = xbmcgui.ListItem('[WNHQ001] Lady Brock Vs Sc@r - Muppet (UK Hardcore)', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/wnhq002.m3u'
    li = xbmcgui.ListItem('[WNHQ002] Double T - Lil Fluffy Cloudz (Drum n Bass)', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/wnhq003.m3u'
    li = xbmcgui.ListItem('[WNHQ003] Force & Styles - Field Of Dreams (Firestrike Drumstep Remix) (Drumstep)', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder6':
    foldername = args['foldername'][0]
    url = 'http://www.whitenoisehq.co.uk/v3/YouTube2.m3u'
    li = xbmcgui.ListItem('[WNHQ Live] DJ Klass-A : Miss-Judged : Double T (UK Hardcore)', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = 'http://www.whitenoisehq.co.uk/v3/YouTube.m3u'
    li = xbmcgui.ListItem('[WNHQ Live] DJ Klass-A - Hard House Power Hour (Hard House)', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    xbmcplugin.endOfDirectory(addon_handle)