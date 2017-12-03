import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')
url = 'http://live-kiss.sharp-stream.com/kiss100.aac'
li = xbmcgui.ListItem('Kiss FM UK - National', iconImage='http://www.industrytrust.co.uk/wp-content/uploads/2014/01/Kiss-logo.jpg', thumbnailImage='http://www.kissfm.md/web/img/site/logo.png')
li.setProperty('fanart_image', 'https://www.taolasvegas.com/files/2016/06/TAO_nightclub-2016-2.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://live-bauer-al.sharp-stream.com/kisstory.aac'
li = xbmcgui.ListItem('Kisstory', iconImage='http://www.bauermedia.co.uk/bauer-emptor/image/upload/c_fit,h_200,w_300/v1437411903/bauer-emptor-keystone-test/brands/logo/oovzr5nyuzckztyolaim.png', thumbnailImage='http://www.kissfm.md/web/img/site/logo.png')
li.setProperty('fanart_image', 'https://www.taolasvegas.com/files/2016/06/TAO_nightclub-2016-2.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://live-kiss.sharp-stream.com/kissfresh.aac'
li = xbmcgui.ListItem('Kiss Fresh', iconImage='http://ukradioonline.com/sites/default/files/radio/logos/logo-kiss-fresh.jpg', thumbnailImage='http://www.kissfm.md/web/img/site/logo.png')
li.setProperty('fanart_image', 'https://www.taolasvegas.com/files/2016/06/TAO_nightclub-2016-2.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)