import xbmc
import urlparse
import sys

try:
        params = urlparse.parse_qs('&'.join(sys.argv[1:]))
        command = params.get('command',None)
except:
        command = None
        
if command and command[0] == 'activate':
        xbmc.executebuiltin('CECActivateSource')
        
elif command and command[0] == 'toggle':
        xbmc.executebuiltin('CECToggleState')

elif command and command[0] == 'standby':
        xbmc.executebuiltin('CECStandby')
