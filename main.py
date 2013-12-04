import json
import cherrypy
import requests

LIGHTS_SERVER = 'http://10.0.1.2/'
GROUP_ENDPOINT='api/newdeveloper/groups/0/action'

on_payload = {"on":True}
off_payload = {"on":False}

class Main(object):
    def on(self):
        url = '{}{}'.format(LIGHTS_SERVER, GROUP_ENDPOINT)
        requests.put(url, data=json.dumps(on_payload))
        return url
    on.exposed = True

    def off(self):
        url = '{}{}'.format(LIGHTS_SERVER, GROUP_ENDPOINT)
        requests.put(url, data=json.dumps(off_payload))
        return url
    off.exposed = True

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(Main())

