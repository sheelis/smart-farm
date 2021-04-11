
import sys
from twisted.web.static import File
from twisted.python import log
from twisted.web.server import Site
from twisted.internet import reactor

from autobahn.twisted.websocket import WebSocketServerFactory, \
    WebSocketServerProtocol

from autobahn.twisted.resource import WebSocketResource

portnr = 8080
serveraddr = "127.0.0.1"

class EchoServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        #print("WebSocket connection request: {}".format(request))
        print("WebSocket connected")

    def onMessage(self, payload, isBinary):
        print("MESSAGE RECEIVED!")
        self.sendMessage(payload, isBinary)
        


if __name__ == '__main__':
    log.startLogging(sys.stdout)

    factory = WebSocketServerFactory(u"ws://"+serveraddr+":"+str(portnr))
    factory.protocol = EchoServerProtocol
    resource = WebSocketResource(factory)

    # we server static files under "/" ..
    root = File(".")
    root.putChild(b"ws", resource)

    site = Site(root)
    reactor.listenTCP(portnr, site)

reactor.run()