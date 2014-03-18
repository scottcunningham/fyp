# Credit to https://github.com/isaaczafuta/pydht

from autobahn.twisted.websocket import WebSocketServerProtocol, \
                                                       WebSocketServerFactory

from pydht import DHT
import sys
import json
import uuid
import tempfile

from twisted.python import log
from twisted.internet import reactor

NUM_NODES = 2
PORT_START = 3001
HOST = "localhost"

node = DHT("localhost", PORT_START + 50, boot_host=HOST, boot_port=PORT_START- 1)

class MyServerProtocol(WebSocketServerProtocol):

   def makeUrl(url):
      return tempfile.mktemp()

   def onConnect(self, request):
      print("Client connecting: {}".format(request.peer))
 
   def onOpen(self):
      print("WebSocket connection open.")
 
   def onMessage(self, payload, isBinary):
      global node
      key = payload.decode('utf-8')
      try:
        value = node[0][key]
        if isBinary:
          print("Binary message received: {} bytes".format(len(payload)))
        else:
          print("Text message received: {}".format(str(payload.decode('utf8'))))

        ## echo back message verbatim
        self.sendMessage(json.dumps({"error" : False, "value" : value}), isBinary)
 
      except KeyError:
        print "Key", key, "not found in DHT"
        # do something error-y, return something bad
        self.sendMessage(json.dumps({"error" : True}), False)
     
      def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {}".format(reason))


if __name__ == '__main__':
   log.startLogging(sys.stdout)


   factory = WebSocketServerFactory("ws://localhost:9000", debug = False)
   factory.protocol = MyServerProtocol

   reactor.listenTCP(9000, factory)
   reactor.run()
