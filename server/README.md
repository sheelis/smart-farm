# MQTT python server

The server.py script is run on the server machine which can even be a headless raspberry pi. It uses asyncio and autobahn to asynchronously transport messages between devices and clients. It relies on mosquitto and paho so they need to be installed and configured first.

## Installation

1. Install Mosquitto broker:
   - ```sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa```
   - ```sudo apt-get update```
   - ```sudo apt-get install mosquitto```
   - ```sudo apt-get install mosquitto-clients```
2. Install Paho Mqtt:
   - ```pip3 install paho-mqtt```
3. Config Mosquitto:
   - ```sudo /etc/init.d/mosquitto stop```  __(stop it)__
   - ```sudo nano /etc/mosquitto/mosquitto.conf```
   - copy contents of the sample conf file 
4. Check if MQTT works
   - ```sudo /etc/init.d/mosquitto stop```
   - ```mosquitto -v```
   - ```netstat –at```  (check for same port number)
5. Add mqtt to Java:
   - [get paho](https://www.eclipse.org/paho/)
6. Start mosquitto properly:            ```mosquitto -c /etc/mosquitto/mosquitto.conf -v```
7. Run html file, check console         ```smart-farm/client/index.html```



## Inspiration:

  - https://mosquitto.org/man/mosquitto-8.html
  - https://www.youtube.com/watch?v=AsDHEDbyLfg
  - http://www.steves-internet-guide.com/install-mosquitto-linux/#install-test
  - http://www.steves-internet-guide.com/into-mqtt-python-client/



## TODO NEXT:

- control ESP over wifi LAN
- control arduinos over USB
- control raspi over wifi LAN
- ROS and ROS2 integration
- store device settings for each user