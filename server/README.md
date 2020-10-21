# New approach: MQTT

___________________________________________

### inspiration:

  - https://mosquitto.org/man/mosquitto-8.html
  - https://www.youtube.com/watch?v=AsDHEDbyLfg
  - http://www.steves-internet-guide.com/install-mosquitto-linux/#install-test
  - http://www.steves-internet-guide.com/into-mqtt-python-client/

### Steps

1. Install Mosquitto broker:
   - sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
   - sudo apt-get update
   - sudo apt-get install mosquitto
   - sudo apt-get install mosquitto-clients
2. Install Paho Mqtt:
   - pip3 install paho-mqtt
3. Config Mosquitto:
   - sudo /etc/init.d/mosquitto stop  __(stop it)__
   - sudo nano /etc/mosquitto/mosquitto.conf
   - copy contents of the sample conf file 
4. Check if MQTT works
   - sudo /etc/init.d/mosquitto stop
   - mosquitto -v
   - netstat –at  (check for same port number)
5. Add mqtt to Java:
   - https://www.eclipse.org/paho/
6. Start mosquitto properly:            mosquitto -c /etc/mosquitto/mosquitto.conf -v
7. Run python pub and sub script:       python3 clent.py
8. Run html file, check console         smart-farm/UI/4-mqtt/index (5).html



- **LOGIN**: UI -> login -> check DB -> return userinfo and rights -> login -> subscribe -> display
- **ADD DEV:** UI logged in -> send info to DB -> shows up on the topic list?


Goal:
- learn python - analysis, data science tools

Progress steps:
1. Pass message to and from an arduino
2. Pass message to and from 2 arduinos and 2 clients
3. Python interceptor script - read all, parse, mock-save to DB, analyze?
4. UI get from DB



## How it works

- run mqtt on a server pc
- then users and devices subscribe to topics and the server sorts out who gets which messages
- web browser html subscribes to everything so that it can monitor and control all


TODO:

- connect arduinos over USB
- connect ESP over wifi LAN
- connect raspi over wifi LAN
- store settings somewhere - users, topics, devices (plan this out a bit)