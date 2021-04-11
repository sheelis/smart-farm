# this script works with multiple clients and closes connection when client disconnects. when client reconnects, the connection continues
# TODO: add server capability

from autobahn.asyncio.websocket import WebSocketServerProtocol
import time


class MyServerProtocol(WebSocketServerProtocol):
    '''When creating server protocol, the
    user defined class inheriting the 
    WebSocketServerProtocol needs to override
    the onMessage, onConnect, et-c events for 
    user specified functionality, these events 
    define your server's protocol, in essence'''

    value = 1
    interval = 1
    opener = True
    wsID = 1

    def onConnect(self, request):
        self.wsID = request.peer
        print(self.wsID + "\t ---> \t " + "Client connected")
        
    async def onOpen(self):
        print(self.wsID + "\t <--> \t " + "WebSocket connection open.")
        while self.opener == True:
            mssg = '{"value":"'+str(MyServerProtocol.value)+'", "interval":"'+str(self.interval)+'"}'
            self.sendMessage(mssg.encode('utf8'))
            print(self.wsID + "\t <--- \t " + mssg)
            MyServerProtocol.value = MyServerProtocol.value + self.interval
            await asyncio.sleep(1)
            

    def onMessage(self,payload,isBinary):
        self.interval = int(payload.decode('utf8'))
        print(self.wsID + "\t ---> \t " + str(payload.decode('utf8')))
        
    
    def connection_lost(self, exc):
        print(self.wsID + "\t >--< \t " +"Connection lost")
        self.opener = False

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))

if __name__ == '__main__':
    import asyncio
    from autobahn.asyncio.websocket import WebSocketServerFactory

    factory=WebSocketServerFactory()
    '''Initialize the websocket factory, and set the protocol to the 
    above defined protocol(the class that inherits from 
    autobahn.asyncio.websocket.WebSocketServerProtocol)'''
    factory.protocol=MyServerProtocol
    '''This above line can be thought of as "binding" the methods
    onConnect, onMessage, et-c that were described in the MyServerProtocol class
    to the server, setting the servers functionality, ie, protocol'''

    loop=asyncio.get_event_loop()
    coro=loop.create_server(factory,'127.0.0.1',9000)
    server=loop.run_until_complete(coro)
    '''Run the server in an infinite loop'''
    try:
        print("started loop")
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.close()