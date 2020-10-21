## Differences: number (value) now is shared by all clients, but the increasing factors can be different
# this is useful to display samereadings, but at different time intervals
# Also now i can start a server by executing twistd -no web --path=5/

#TODO: on refresh of webpage it treats it as if new client connected without closing the old one
#TODO try it without asyncio


from autobahn.asyncio.websocket import WebSocketServerProtocol, \
    WebSocketServerFactory


portnr = 9000
serveraddr = "127.0.0.1"


class MyServerProtocol(WebSocketServerProtocol):

    vall = 1
    number = 1
    
    def onConnect(self, request):
        print("Client connected: {0}".format(request.peer))

    async def onOpen(self):
        print("WebSocket connection open.")
        #number = 1
        #vall = 1
        
        while True:
            mssg = '{"value":"'+str(MyServerProtocol.number)+'", "interval":"'+str(MyServerProtocol.vall)+'"}'
            self.sendMessage(mssg.encode('utf8'))
            print(mssg)
            MyServerProtocol.number = MyServerProtocol.number+MyServerProtocol.vall
            await asyncio.sleep(1)

    def onMessage(self, payload, isBinary):
        MyServerProtocol.vall = int(payload.decode('utf8'))
        print(str(MyServerProtocol.vall))


    # def connection_lost(self, *a):
    #     print("conn lost")

    # def onCloseFrame(self, wasClean, reason):
    #     print("frame closed")
        

    def onClose(self, wasClean, code, reason):
        #self.sendClose(code=None, reason=None)
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