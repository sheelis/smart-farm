
from autobahn.asyncio.websocket import WebSocketServerProtocol, \
    WebSocketServerFactory



portnr = 9000
serveraddr = "127.0.0.1"

class MyServerProtocol(WebSocketServerProtocol):
    vall = 1
    
    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    async def onOpen(self):
        print("WebSocket connection open.")
        number = 1
        
        while True:
            mssg = '{"time":"'+str(number)+'"}'
            self.sendMessage(mssg.encode('utf8'))
            print(mssg+ " "+ str(self.vall))
            number = number+self.vall
            await asyncio.sleep(1)

    def onMessage(self, payload, isBinary):
        self.vall = int(payload.decode('utf8'))
        print(str(self.vall))

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))

if __name__ == '__main__':
    print("starts now")
    import asyncio

    #factory = WebSocketServerFactory(u"ws://127.0.0.1:9000")
    factory = WebSocketServerFactory(u"ws://"+serveraddr+":"+str(portnr))
    factory.protocol = MyServerProtocol

    loop = asyncio.get_event_loop()
    #coro = loop.create_server(factory, '0.0.0.0', portnr)
    coro = loop.create_server(factory, serveraddr, portnr)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
loop.close()