# Smart farm

IoT System that allows live monitoring, storing, analyizing of current weather (e.g. wind speed) and deployed system status (e.g. battery charge) and predictions to achieve custom set goals by the user (e.g. use electric power more efficiently).

The main idea is to have a locally run IoT dashboard to easily add and control your IoT devices.

The analysis and prediction will be deployed as an add-on python library so that it can be updated separately.
The option to update / synchronize with online services and databases is also possible and planned for, but not yet implemented as the goal is to avoid the need for all unnecessary connectivity in order to increase system rigidity, speed, cost of operation and full freedom to tinker and modify the code.


## Running it

On the server run ``` python3 /server/server.py```
On the client device open ```/client/index.html``` in your web browser to see the dashboard.
Program your IoT device to send data or receive commands in JSON format (see arduino code example)
Then add your IoT devices and map the data points to variables

Adding your IOT devices:

![adding devices](Screenshot-devices.png)



## Relevant data nalysis and predictions 

Useful applications for a small modernized household / hobby lot.

- Rain water tanks
  - calculate rates of consumption
  - fetch past weather data to learn how much rainfall yielded how many liters of water
  - gather past and future data to predict draugths or storms
  - suggest appropriate actions to user (try to save water or use more water before storm)
  - calculate if predictions were correct when time comes
  - measure water temperature, to find best times to enable water heater
- Solar or wind power
  - calculate rates of consumption and accumulation
  - gather weather data, predict shortages, maintenance, potentially useful improvements (more batteries, more panels, etc.) 
  - regulate consumption (turn devices on or off based on rules and thresholds)
- Greenhouse 
  - temperature, light and air humidity levels
  - automated watering, misting, ventilation, etc




## Software functionality

- _System_
    - __server scripts__
        - server (center)
            - duplex with all clients
              - clients share: sensor readings, time, weather data
              - admin can set: which client sees and controls what
            - get and send messages / commands
            - talk to other scripts
            - manage users
        - reader / actor (hardware)
            - gets sensor readings
            - sends commands to hardware
        - saver, retriever
            - operates database
            - talks to server, reader, analyzer
            - backup of database to cloud etc
        - analyzer (local)
            - future predictions
            - history analysis
        - fetcher
            - get info from internet
                - weather
                - time
                - farming events
    - __client scripts__
        - server requires login
        - communication with server
        - graphing
    - __database__
        - sensor data
        - actuator data / commands
        - settings
            - client side
            - server side
            - user preferences
            - user info (name, pwd, logon times)
        - user added notes
        - predictions
        - future weather?

## Hardware needed

- Server:
  - raspberry
  - router
- Sensors:
  - water level
  - battery charge level
  - battery voltage
  - light level
  - wind speed
  - temperature
- Actuators
  - relays
  - motors
  - leds
