# Credit to https://github.com/isaaczafuta/pydht

from autobahn.twisted.websocket import WebSocketServerProtocol, \
                                                       WebSocketServerFactory

from pydht import DHT
import sys
import json
import tempfile
from join_network import get_keys

from twisted.python import log
from twisted.internet import reactor

NUM_NODES = 2
PORT_START = 3001
HOST = "localhost"

print "Creating node, joining network"
keys = get_keys("keys")
node = DHT("localhost", PORT_START + 50, boot_host=HOST, boot_port=PORT_START- 1, keys=keys)
print "Done."

class MyServerProtocol(WebSocketServerProtocol):

   def makeUrl(self):
       return tempfile.NamedTemporaryFile()

   def onConnect(self, request):
      print("Client connecting: {}".format(request.peer))
 
   def onOpen(self):
      print("WebSocket connection open.")
 
   def onMessage(self, payload, isBinary):
      global node
      raw_message = str(payload) #.decode('utf8', errors='ignore')
      message = json.loads(raw_message)

      print "Got message: {}".format(raw_message)
      
      key = message["key"]
      
      if message["type"] == "downvote":
          print "downvote", key
          node.downvote(key)

      if message["type"] == "publish":
          print "publish req"
          content = str(message["body"]) #.encode('utf8', errors='ignore')
          key = str(key) #).encode('utf8', errors='ignore')
          print "hash is", key
          print "content is", content
          print "storing now"
          content = json.dumps(content)
          node.publish(key, content)
          self.sendMessage(json.dumps({"type" : "publish", "error" : False, "value" : key}), False)
          print "stored"

      elif message["type"] == "lookup":
          print "lookup"
          try:
            print "Looking up key {}".format(key)
            value = node.retrieve(key)
            value = json.loads(value)
            print "decrypted is", value
            self.sendMessage(json.dumps({"type" : "lookup", "error" : False, "value" : value}), isBinary)
     
          except KeyError:
            print "Key not found in DHT"
            # do something error-y, return something bad
            self.sendMessage(json.dumps({"type" : "lookup", "error" : True, "value" : "key not found!"}), False)
    
   def onClose(self, wasClean, code, reason):
     print("WebSocket connection closed: {}".format(reason))


if __name__ == '__main__':
   log.startLogging(sys.stdout)


   print "Creating websocket frontend handler"
   factory = WebSocketServerFactory("ws://localhost:9000", debug = False)
   factory.protocol = MyServerProtocol
   print "Done, starting up"

   reactor.listenTCP(9000, factory)
   reactor.run()
