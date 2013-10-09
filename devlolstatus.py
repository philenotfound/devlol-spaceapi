# coding: latin-1

import json
import urllib2
import re

def application(environ, start_response):

        def get_state():
           try:
             reponse = urllib2.urlopen('http://mars.zauberfisch.at/devlol/status.php','',10)
             answer = reponse.read()
             #strip html
             answer = re.sub('<[^<]+?>', '', answer)
             if answer.endswith('open'):
               return True
             else:
               return False
           except:
             return False

        minimal_space_api_data = {
            "api": "0.13",
            "space": "DevLol",
            "logo": "https://devlol.org/static_wiki/DevLoL.png",
            "url": "https://devlol.org",
            "location": {
                "address": "Hofgasse 19, 4020 Linz, Austria",
                "lon": 14.28383,
                "lat": 48.30573
            },
            "contact": {
                "ml": "devlol-orga@lists.servus.at",
                "irc": "ircs://irc.servus.at:6667/devlol"
            },
            "cache": {
                "schedule": "m.02"
            },
            "issue_report_channels": [
                "ml"
            ],
            "state": {
                "open": get_state()
            }
        }

        start_response('200 OK', [('content-type', 'application/json')])
        return json.dumps(minimal_space_api_data,indent=4,sort_keys=True,separators=(',',': '))
