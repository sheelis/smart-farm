import paho.mqtt.client as mqtt #import the client1
import time

def on_message(client, userdata, message):
    print(" < Received: \t",message.topic, str(message.payload.decode("utf-8")))
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
def on_publish(client, userdata, message):
    print(" > Published: \t")
    pass

def on_disconnect(client, userdata, rc):
   print("client disconnected ok")

#broker_address="iot.eclipse.org" #use external broker
broker_address="127.0.0.1" 
topic1="house/bulb1"


# client = mqtt.Client(client_id=””, clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)
client = mqtt.Client("Brains")         #create new instance
client.on_message=on_message            #attach function to callback
client.on_publish=on_publish
client.on_disconnect = on_disconnect

print(" - Connecting to broker:",broker_address)
# client.connect(host, port=1883, keepalive=60, bind_address="")
try:
    client.connect(broker_address)          #connect to broker
    client.loop_start()                     #start the loop

    print(" - Subscribing to: \t",topic1)
    client.subscribe(topic1)
    print(" --------------------------------------- ")

    client.publish(topic1,'{"greenhouse1-temp1":"100"}')

    time.sleep(8)
    client.loop_forever()    #stop the loop


except:
    print("   - FAILED")
print(" --------------------------------------- ")

client.disconnect()
print(" - Exiting.")    

