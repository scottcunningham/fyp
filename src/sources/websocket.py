# Credit to https://github.com/tavendo/AutobahnPython

from autobahn.twisted.websocket import WebSocketServerProtocol, \
                                               WebSocketServerFactory

class MyServerProtocol(WebSocketServerProtocol):
 
   def onConnect(self, request):
      print("Client connecting: {}".format(request.peer))
 
   def onOpen(self):
      print("WebSocket connection open.")
 
   def onMessage(self, payload, isBinary):
      if isBinary:
         print("Binary message received: {} bytes".format(len(payload)))
      else:
         print("Text message received: {}".format(payload.decode('utf8')))
 
      ## echo back message verbatim
      self.sendMessage(payload, isBinary)
 
   def onClose(self, wasClean, code, reason):
      print("WebSocket connection closed: {}".format(reason))


if __name__ == '__main__':
   import sys

   from twisted.python import log
   from twisted.internet import reactor

   log.startLogging(sys.stdout)

   factory = WebSocketServerFactory("ws://localhost:9000", debug = False)
   factory.protocol = MyServerProtocol

   reactor.listenTCP(9000, factory)
   reactor.run()


