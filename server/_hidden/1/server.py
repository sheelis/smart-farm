'''Communicates with clients'''

from autobahn.asyncio.websocket import WebSocketServerProtocol
import time
import json


# My imports:
from lib import arduino_serial

# Global vars:

datatype_reading = "reading"
datatype_setting = "setting"
datatype_alert = "alert"
codeID = "SERVER: \t "


class MyServerProtocol(WebSocketServerProtocol):
    '''Class for tunneling data between client and devices'''

    interval = 1        # webpage update interval in seconds (default = 1)
    opener = False      # flag: connection is active
    usrID = ""          # placeholder for websocket request.peer
    username = ""       # placeholder current username
    rawRX = ""          # placeholder for raw input from client
    nanos = []          # create a list for storing found arduinos for later reference [handle,ID]
    

    def FindConnectDevices(self):
        ''' Talks to the hardware via libraries to get handles of all devices so that they can be addressed and talked to'''
        # this should get called on startup of server and when new device added
        self.nanos = arduino_serial.find("")
        
    def GetSetSettings(self):
        '''Reads sever and user settings from DB and sends them to user. Maybe better a separate file?'''

        # Get settings:
        # jsonfile = open('data.json')
        # jsonSettings = json.load(jsonfile)  # convert str to json  
        # jsonfile.close()
        # https://www.tutorialspoint.com/How-do-I-loop-through-a-JSON-file-with-multiple-keys-sub-keys-in-Python
    
        # Send settings:
        #  should iteratively create json string of only new settings
        jsonedsettings = '{"'+datatype_setting+'": [{"ui": [{"name":"interval", "value": '+ str(self.interval)+'}]}]}'
        print(codeID+self.usrID + "\t <--- \t " + jsonedsettings)        # send reply to server of current settings
        self.sendMessage(jsonedsettings.encode('utf8'))

    def handleRX(self, RX):
        '''handle incoming data received from client, then separates datatype and calls appropriate dunction (settings, command, etc)'''
        jsonload = json.loads(RX)  # convert str to json  

        if self.username == "":
            try:
                jsonload["username"]
                self.opener = True
                self.username = jsonload["username"]
                self.usrID = self.usrID+"-"+self.username
                print(codeID+self.usrID + "\t ---> \t " + "Client authenticated")
            except:
                pass 

        # should iteratively decode the clients message here:     
        for dtype in jsonload:
            # print(dtype)
            # save new settings to DB
            try:
                jsonload["interval"]
                self.interval = jsonload["interval"]       # set update interval to the value of "interval"
            except:
                pass 
            
        self.GetSetSettings()
   
    def onConnect(self, request):
        '''Fires when user opens browser to the server's address'''
        self.usrID = str(request.peer)
        print(codeID+self.usrID + "\t ---> \t " + "Client connected")
        
    async def onOpen(self):
        '''Sends data to client'''
        print(codeID+self.usrID + "\t <--> \t " + "WebSocket client connection open.")
        while self.opener == False:
            await asyncio.sleep(0.1) # wait for username to arrive
        while self.opener == True:
            # mssg = reader.Nano.getReading(reader.Nano)
            rdng = self.nanos[0][0].get_reading()
            data_type = "reading"
            readingID1 = "temp1"
            readingID2 = "humidity"
            mssg = '{"'+data_type+'": [{"'+str(self.nanos[0][1])+'": [{"name":"'+readingID2+'", "value": 10}, {"name":"'+readingID1+'", "value": '+ str(rdng)+'}]}]}'
        
            print(codeID+self.usrID + "\t <--- \t " + mssg)
            self.sendMessage(mssg.encode('utf8'))
            await asyncio.sleep(self.interval)             

    async def onMessage(self,payload,isBinary):
        '''Fires when client has sent something to server'''
        self.rawRX = (payload.decode('utf8'))
        print(codeID+self.usrID + "\t ---> \t " + str(payload.decode('utf8')))
        self.handleRX(self.rawRX)
        
    def connection_lost(self, exc):
        '''Client disconnected, closed browser or refreshed page'''
        print(codeID+self.usrID + "\t >--< \t Client lost connection!")
        self.opener = False

    def onClose(self, wasClean, code, reason):
        print(codeID+"WebSocket client connection closed: {0}".format(reason))
        # deauth user

if __name__ == '__main__':
    import asyncio
    from autobahn.asyncio.websocket import WebSocketServerFactory

    print(codeID+"STARTED -------------------------------------------------------------------")

    factory=WebSocketServerFactory()
    '''Initialize the websocket factory, and set the protocol to the above defined protocol(the class that inherits from autobahn.asyncio.websocket.WebSocketServerProtocol)'''
    factory.protocol=MyServerProtocol
    '''This above line can be thought of as "binding" the methods onConnect, onMessage, et-c that were described in the MyServerProtocol class to the server, setting the servers functionality, ie, protocol'''

    loop=asyncio.get_event_loop()
    # coro=loop.create_server(factory,'127.0.0.1',9000)
    coro=loop.create_server(factory,'192.168.1.101',9000)
    server=loop.run_until_complete(coro)
    '''Run the server in an infinite loop'''
    MyServerProtocol.FindConnectDevices(MyServerProtocol)
    try:
        print(codeID+"WEBSOCKET LOOP STARTED")
        loop.run_forever()
    except KeyboardInterrupt:
        pass
        # add some grace
        print(codeID+"YOU QUIT FORCEFULLY")
    finally:
        server.close()
        loop.close()