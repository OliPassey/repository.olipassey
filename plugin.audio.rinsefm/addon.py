import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'http://streamer.dgen.net:8000/rinseradio.m3u'
li = xbmcgui.ListItem('Rinse.FM', iconImage='http://in-reach.co.uk/wp-content/uploads/2014/02/rinse-fm-logo-620x400.png', thumbnailImage='http://in-reach.co.uk/wp-content/uploads/2014/02/rinse-fm-logo-620x400.png')
li.setProperty('fanart_image', 'http://in-reach.co.uk/wp-content/uploads/2014/02/rinse-fm-logo-620x400.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)