import blink1
import random
import time
import jb_http_getter

host="api.steampowered.com:80"
#url="/ISteamUser/GetPlayerSummaries/v0002/?key=2D23CE3CDE0849FCB5A7F2EA10100BD1&steamids=76561197970715856"
url="/ISteamUser/GetPlayerSummaries/v0002/?key=2D23CE3CDE0849FCB5A7F2EA10100BD1&steamids=STEAMID"

while 1:
    dev = blink1.open()
    f = open('steamids.txt', 'r')
    while 1:
        l = f.readline()
        if l == None or len(l) <= 0:
            break
        if not l.startswith('#'):
            blink1.fadeToRGB(dev, 900, 0x00, 0x00, 0x00)
            time.sleep(1)
            l = l.replace('\n', '')
            color={'red':0, 'green':0, 'blue':0x00}
            try:
                body = jb_http_getter.get_url(host, url.replace("STEAMID",l))
            except:
                body = ''
            print body
            ###offline
	    if body.find('personastate":0') >= 0:
                color['red'] = 0xff
		color['blue'] = color['green'] = 0
            ###online
            elif body.find('personastate":1') >= 0 and body.find('gameextrainfo":') < 0:
                color['blue'] = 0xff
		color['red'] = color['green'] = 0
	    ###busy
            elif body.find('personastate":2') >= 0 and body.find('gameextrainfo":') < 0:
		color['red'] = color['blue'] = 0xff
		color['green'] = 0
	    ### away/snoooze
            elif (body.find('personastate":3') >= 0 or body.find('personastate": 4') >= 0) and body.find('gameextrainfo":') < 0:
		color['red'] = color['blue'] = 0xff
		color['green'] = 0
	    ###possible to be 'away' and in a game..
            elif body.find('gameextrainfo":') >= 0 and body.find('personastate":1') >= 0:
	        color['green'] = color['blue'] = 0xff
            elif body.find('gameextrainfo":') >= 0:
                color['green'] = 0xff
	    ###in-a-game, or something else...
            else:
		color['red'] = color['green'] = color['blue'] = 0xff
            
            blink1.fadeToRGB(dev, 900, color['red'], color['green'], color['blue'])
            time.sleep(2)
    f.close()
    blink1.fadeToRGB(dev,900, 0x00, 0x00, 0x00)
    time.sleep(5)
    blink1.close(dev)

        
