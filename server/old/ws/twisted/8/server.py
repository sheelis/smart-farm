# this script works with multiple clients and closes connection when client disconnects. when client reconnects, the connection continues
# TODO: add server capability

from autobahn.asyncio.websocket import WebSocketServerProtocol
import time
import json


class Devices():
    temperature = 1
    command = ""
    def getReading(self):
        self.temperature += 1
        return '{"value":'+ str(self.temperature)+'}'
    def setCommand(self, CMD):
        print(str(CMD))



class MyServerProtocol(WebSocketServerProtocol):
    '''When creating server protocol, the user defined class inheriting the WebSocketServerProtocol needs to override the onMessage, onConnect, et-c events for user specified functionality, these events define your server's protocol, in essence'''
    interval = 1    # webpage update interval in seconds
    opener = True   # flag: connection is active
    wsID = 1        # placeholder for websocket request.peer
    rawRX = ""      # placeholder for raw input from client

    def handleRX(self, RX):
        '''handle incoming data received from client'''
        jsonload = json.loads(RX)                       # convert str to json        
        self.interval = int(jsonload["interval"])       # set update interval to the value of "interval"

        reply = '{"interval":'+ str(self.interval) +'}'      # creating a reply to say that it is updated
        #jsonload = str(jsonload).replace("'", '"')      # this sucks (replacing single with double quotes)
        print(self.wsID + "\t <--- \t " + reply)        # send reply to server of current interval
        self.sendMessage(reply.encode('utf8'))
        

    def onConnect(self, request):
        self.wsID = str(request.peer)
        print(self.wsID + "\t ---> \t " + "Client connected")
        
    async def onOpen(self):
        '''send data to client'''
        print(self.wsID + "\t <--> \t " + "WebSocket connection open.")
        while self.opener == True:
            mssg = Devices.getReading(Devices)
            print(self.wsID + "\t <--- \t " + mssg)
            self.sendMessage(mssg.encode('utf8'))
            await asyncio.sleep(self.interval)          

    def onMessage(self,payload,isBinary):
        self.rawRX = (payload.decode('utf8'))
        print(self.wsID + "\t ---> \t " + str(payload.decode('utf8')))
        self.handleRX(self.rawRX)
        
    def connection_lost(self, exc):
        print(self.wsID + "\t >--< \t Client lost connection!")
        self.opener = False

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))

if __name__ == '__main__':
    import asyncio
    from autobahn.asyncio.websocket import WebSocketServerFactory

    factory=WebSocketServerFactory()
    '''Initialize the websocket factory, and set the protocol to the above defined protocol(the class that inherits from autobahn.asyncio.websocket.WebSocketServerProtocol)'''
    factory.protocol=MyServerProtocol
    '''This above line can be thought of as "binding" the methods onConnect, onMessage, et-c that were described in the MyServerProtocol class to the server, setting the servers functionality, ie, protocol'''

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