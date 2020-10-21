# Smart farm

System that allows live monitoring, storing, analyizing and predicting of grid and off-grid elements data locally and or centrally over internet.

Examples
- rain water tank: 
  - calculate rates of consumption
  - fetch past weather data to learn how much rainfall yielded how many liters of water
  - gather past and future data to predict draugths or storms
  - suggest appropriate actions to user (try to save water or use more water before storm)
  - calculate if predictions were correct
  - measure water temperature, to find best times to use devices that heat water
- solar power: 
  - calculate rates of consumption
  - gather weather data, predict shortages, maintenance, useful improvements of solar system (more batteries, more panels, etc.) 
  - regulate consumption (turn devices on or off)


## Software


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
            - get sensor readings
            - send commands to hardware
        - saver, retriever
            - operate database
            - talks to server, reader, analyzer
            - backup database to cloud etc
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

## Hardware

- Brain:
  - firefly
  - raspberry
  - flatscreen?
  - sim card
  - small router or AP mode? (comms with all distant sensors)
- sensors:
  - water level
  - battery charge level
  - battery voltage
  - light level
  - wind speed
  - temperature
- actuators
  - relays
  - motors
  - leds
