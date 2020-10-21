
#include <SPI.h>
#include <Ethernet.h>
#include <PubSubClient.h>
#include "DHT.h"

// Update these with values suitable for your network.
byte mac[]    = {  0xDE, 0xED, 0xBA, 0xFE, 0xFE, 0xED };
IPAddress ip(192, 168, 1, 188);
IPAddress server(192, 168, 1, 102);



#define ledPin 9
#define DHTPIN 2     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
DHT dht(DHTPIN, DHTTYPE);

EthernetClient ethClient;
PubSubClient client(ethClient);

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print(" : ");
  String message_full= "";
  for (int i=0;i<length;i++) {
    message_full = message_full+(char)payload[i];
  }
  Serial.print(message_full); 
  Serial.println("]"); 

  if (String(topic) == "rgbled"){
    if (message_full == "blue"){
      digitalWrite(ledPin, HIGH);
    } else if (message_full == "off"){
     digitalWrite(ledPin, LOW);
    } else {
      Serial.println("unexpected message received");
    }
  } else {
    Serial.println("no reaction to this topic");
  }
}




void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("arduinoClient1")) {
      Serial.println("connected");
      client.subscribe("rgbled");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup()
{
  Serial.begin(57600);

  client.setServer(server, 1883);
  client.setCallback(callback);

  Ethernet.begin(mac, ip);
  Serial.println("Ethernet started");
  // Allow the hardware to sort itself out
  
  dht.begin();

  pinMode(ledPin, OUTPUT);
  delay(1500);
}

void loop()
{
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  float temp = dht.readTemperature();
  client.publish("house-temp", String(temp).c_str(), true);
  delay(100);
  float humid = dht.readHumidity();
  client.publish("house-humid", String(humid).c_str(), true);
  
  delay(100);
  
}
