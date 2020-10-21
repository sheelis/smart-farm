import paho.mqtt.client as mqtt #import the client1
import time

def on_message(client, userdata, message):
    print("- Message:",message.topic, str(message.payload.decode("utf-8")))
    
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)


#broker_address="iot.eclipse.org" #use external broker
broker_address="127.0.0.1" 
topic1="house/bulb1"


# client = mqtt.Client(client_id=””, clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)
client = mqtt.Client("Brains 2222")         #create new instance
client.on_message=on_message            #attach function to callback


print("Connecting to broker")
# client.connect(host, port=1883, keepalive=60, bind_address="")
client.connect(broker_address, keepalive=60)          #connect to broker
client.loop_start()                     #start the loop

print("Subscribing to topic",topic1)
client.subscribe(topic1)

print("Publishing to topic",topic1)
client.publish(topic1,"OFF")


time.sleep(8)

print("Publishing to topic",topic1)
client.publish(topic1,"AFTER TIME")
time.sleep(3) 

client.loop_stop()    #stop the loop