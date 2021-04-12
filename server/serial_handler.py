'''arduino to web browser communication'''

import paho.mqtt.client as mqtt 
import time
import json

# My imports:
from lib import arduino_serial



# Important variables
broker_address="127.0.0.1" # My mqtt broker address on LAN


# Global strings:
datatype_reading = "reading"
datatype_setting = "setting"
datatype_alert = "alert"
codeID = "SERVER: \t "



def on_message(client, userdata, message):
    print(" < Received: \t",message.topic, str(message.payload.decode("utf-8")))
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
def on_publish(client, userdata, message):
    print(" > Published: \t something")
    pass

def on_disconnect(client, userdata, rc):
   print("client disconnected ok")

def FindConnectDevices(self):
    ''' Talks to the hardware via libraries to get handles of all devices so that they can be addressed and talked to'''
    # this should get called on startup of server and when new device added
    self.nanos = arduino_serial.find("")

def handleRX(self, RX):
    '''handle incoming data received from client, then separates datatype and calls appropriate function (settings, command, etc)'''
    jsonload = json.loads(RX)  # convert str to json  

    if self.username == "":
        try:
            jsonload["username"]
            self.opener = True
            self.username = jsonload["username"]
            self.usrID = self.usrID+"-"+self.username
            print(codeID+self.usrID + "\t ---> \t " + "OK. User authrized")
        except:
            pass 

    # should iteratively decode the clients message here:     
    for dtype in jsonload:
        # print(dtype)
        # save new settings to DB
        try:
            jsonload["interval"]
            self.interval = jsonload["interval"]       # data update interval is programmed to be the user's set number
        except:
            pass 
        
    # self.GetSetSettings()

def handleTX():
    rdng = self.nanos[0][0].get_reading()
    data_type = "reading"
    readingID1 = "temp1"
    readingID2 = "humidity"
    mssg = '{"'+data_type+'": [{"'+str(self.nanos[0][1])+'": [{"name":"'+readingID2+'", "value": 10}, {"name":"'+readingID1+'", "value": '+ str(rdng)+'}]}]}'

    print(codeID+self.usrID + "\t <--- \t " + mssg)
    self.sendMessage(mssg.encode('utf8'))   
    

# def GetSetSettings(self):
#     '''Reads sever and user settings from DB and sends them to user. Maybe better a separate file?'''

#     # Get settings:
#     # jsonfile = open('data.json')
#     # jsonSettings = json.load(jsonfile)  # convert str to json  
#     # jsonfile.close()
#     # https://www.tutorialspoint.com/How-do-I-loop-through-a-JSON-file-with-multiple-keys-sub-keys-in-Python

#     # Send settings:
#     #  should iteratively create json string of only new settings
#     jsonedsettings = '{"'+datatype_setting+'": [{"ui": [{"name":"interval", "value": '+ str(self.interval)+'}]}]}'
#     print(codeID+self.usrID + "\t <--- \t " + jsonedsettings)        # send reply to server of current settings
#     self.sendMessage(jsonedsettings.encode('utf8'))

    


# aquire topics from storage:
topics = ["rgbled","house-humid", "house-temp"]


# client = mqtt.Client(client_id=””, clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)
client = mqtt.Client("--[ PYTHON TO IOT ]--")         #create new instance
client.on_message=on_message            #attach function to callback
client.on_publish=on_publish
client.on_disconnect = on_disconnect

print(" - Connecting to broker:",broker_address)
# client.connect(host, port=1883, keepalive=60, bind_address="")
try:
    client.connect(broker_address)          #connect to broker
    client.loop_start()                     #start the loop

    # for name in topics:
    print(" - Subscribing to: \t",topics[0])
    client.subscribe(topics[0])



    print(" --------------------------------------- ")

    # get readings from USB devices
    client.publish(topics[2],'hi from client.py')
    client.publish(topics[1],'94')

    time.sleep(8)

        
    



    client.loop_forever()    #stop the loop
except:
    print("   - FAILED")
print(" --------------------------------------- ")

client.disconnect()
print(" - Exiting.")    

