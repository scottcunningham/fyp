# Credit to https://github.com/isaaczafuta/pydht

from autobahn.twisted.websocket import WebSocketServerProtocol, \
                                                       WebSocketServerFactory

from pydht import DHT
import sys
import json
import tempfile

from twisted.python import log
from twisted.internet import reactor

NUM_NODES = 2
PORT_START = 4000
HOST = "localhost"

print "Creating node, joining network"
node = DHT("localhost", PORT_START + 50)
node.bootstrap("localhost", PORT_START)
print "Done."

class MyServerProtocol(WebSocketServerProtocol):

   def makeUrl(self):
       return tempfile.NamedTemporaryFile()

   def onConnect(self, request):
      print "Client connecting: {}".format(request.peer)

   def onOpen(self):
      print "WebSocket connection open."

   def onMessage(self, payload, isBinary):
      global node
      raw_message = str(payload) #.decode('utf8', errors='ignore')
      message = json.loads(raw_message)

      print "Got message: {}".format(raw_message)

      if message["type"] == "downvote":
          key = message["key"]
          print "downvote", key
          node.downvote(key)

      if message["type"] == "publish":
          print "publish req"
          content = str(message["body"]) #.encode('utf8', errors='ignore')
          print "content is", content
          print "storing now"
          content = json.dumps(content)
          key = node.publish(content)
          self.sendMessage(json.dumps({"type" : "publish", "error" : False, "value" : key}), False)
          print "stored"

      elif message["type"] == "lookup":
          key = message["key"]
          print "lookup"
          try:
            print "Looking up key {}".format(key)
            value = node.retrieve(key)
            value = json.loads(value)
            print "value is", value
            self.sendMessage(json.dumps({"type" : "lookup", "error" : False, "value" : value, "key" : key}), isBinary)
          except KeyError:
            print "Key not found in DHT"
            self.sendMessage(json.dumps({"type" : "lookup", "error" : True, "value" : "key not found!"}), False)
          except ValueError:
            print "hmac failed"
            self.sendMessage(json.dumps({"type" : "lookup", "error" : True, "value" : "node can't verify message HMAC!"}), False)

   def onClose(self, wasClean, code, reason):
     if wasClean:
         print "WebSocket conn closed cleanly [{}]".format(code)
     else:
         print "WebSocket conn closed due to error [{}]: {}".format(code, reason)

if __name__ == '__main__':
   log.startLogging(sys.stdout)


   print "Creating websocket frontend handler"
   factory = WebSocketServerFactory("ws://localhost:9000", debug = False)
   factory.protocol = MyServerProtocol
   print "Done, starting up"

   reactor.listenTCP(9000, factory)
   reactor.run()
