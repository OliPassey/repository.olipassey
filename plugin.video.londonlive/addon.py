import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'http://bcoveliveios-i.akamaihd.net/hls/live/217434/3083279840001/master.m3u8'
li = xbmcgui.ListItem('London Live', iconImage='http://whitenoisehq.co.uk/londonlivelogo.png', thumbnailImage='http://whitenoisehq.co.uk/londonlivelogo.png')
li.setProperty('fanart_image', 'fanart.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)