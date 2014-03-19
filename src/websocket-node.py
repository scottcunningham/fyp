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

import json
import hashlib

NUM_NODES = 2
PORT_START = 3001
HOST = "localhost"

node = DHT("localhost", PORT_START + 50, boot_host=HOST, boot_port=PORT_START- 1)

class MyServerProtocol(WebSocketServerProtocol):

   def makeUrl(self):
       return tempfile.NamedTemporaryFile()

   def onConnect(self, request):
      print("Client connecting: {}".format(request.peer))
 
   def onOpen(self):
      print("WebSocket connection open.")
 
   def onMessage(self, payload, isBinary):
      global node
      raw_message = payload.decode('utf-8')
      message = json.loads(raw_message)

      print "Got message: {}".format(raw_message)
      
      key = message["body"]
      
      if message["type"] == "publish":
          print "publish req"
          content = message["body"]
          print "storing now"
          key = node.publish(content, content) 
          print "hash is", key
          self.sendMessage(json.dumps({"type" : "publish", "error" : False, "value" : key}), False)
          print "stored"

      elif message["type"] == "lookup":
          print "lookup"
          try:
            print "Looking up key {}".format(key)
            value = node[key]
            if isBinary:
              print("Binary message received: {} bytes".format(len(payload)))
            else:
              print("Text message received: {}".format(str(payload.decode('utf8'))))

            ## echo back message verbatim
            self.sendMessage(json.dumps({"type" : "lookup", "error" : False, "value" : value}), isBinary)
     
          except KeyError:
            print "Key not found in DHT"
            # do something error-y, return something bad
            self.sendMessage(json.dumps({"type" : "lookup", "error" : True, "value" : "key not found!"}), False)
         

      def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {}".format(reason))


if __name__ == '__main__':
   log.startLogging(sys.stdout)


   factory = WebSocketServerFactory("ws://localhost:9000", debug = False)
   factory.protocol = MyServerProtocol

   reactor.listenTCP(9000, factory)
   reactor.run()
