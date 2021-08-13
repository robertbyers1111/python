#!/usr/bin/python3

import json
import requests
import pprint
import websocket
import sys

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def showdir(obj):
  print()
  for x in sorted(str(dir(obj)).split(',')):
    print(x)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def doitjson(url):
  resp = requests.get(url)
  o = resp.json()
  print()
  print('['+url+']')
  for k,v in o.items():
    print('   ',k+':',v)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def doittext(url):
  resp = requests.get(url)
  print()
  print('['+url+']')
  print()
  for line in str(resp.text).split('<'):
    print('<'+line)

#   +---------+
#---| M A I N |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   +---------+

#showdir(requests.models.Response)
#doitjson('https://status.github.com/api/status.json')
#doittext('https://news.google.com/news/?ned=us&gl=US&hl=en')
doittext('https://www.hockey-reference.com/players/m/modanmi01.html')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#FROM: https://stackoverflow.com/questions/43548992/how-can-i-tell-that-the-page-has-finished-loading

#tablist = json.loads(requests.get("http://%s:%s/json" % ("localhost", 9222)).text)
#print(tablist)
#wsurl = tablist[0]['webSocketDebuggerUrl']
#conn = websocket.create_connection(wsurl)
#navcom = json.dumps({"id":0, "method":"Network.enable"})
#conn.send(navcom)
#navcom = json.dumps({"id":1, "method":"Page.enable"})
#conn.send(navcom)
#navcom = json.dumps({"id":2, "method":"Page.navigate", "params":{"url":sys.argv[1]}})
#conn.send(navcom)
#
#while True:
#    s = conn.recv()
#    packet = json.loads(s)
#    if packet.get('method') == 'Page.loadEventFired':
#        break
#    print(s)
