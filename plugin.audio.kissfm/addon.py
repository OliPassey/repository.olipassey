import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'audio')

url = 'http://tx.whatson.com/icecast.php?i=kisstorylow.mp3'
li = xbmcgui.ListItem('Kisstory', iconImage='http://whitenoisehq.co.uk/kisstory.png', thumbnailImage='http://whitenoisehq.co.uk/kisstory.png')
li.setProperty('fanart_image', 'http://whitenoisehq.co.uk/kissbg.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://tx.whatson.com/icecast.php?i=kissnationallow.mp3'
li = xbmcgui.ListItem('Kiss FM UK - National', iconImage='http://whitenoisehq.co.uk/kisslogo.png', thumbnailImage='http://whitenoisehq.co.uk/kisslogo.png')
li.setProperty('fanart_image', 'http://whitenoisehq.co.uk/kissbg.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)