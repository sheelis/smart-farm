# UI


- _UI_
    - cross-platform (web) dashboard
    - cross device (mobile compatible design)
    - multi-user (each user has own settings)
    - live monitoring
    - easy to add more sensors, actuators
    - sections: tabs or pages? 
        - __Dashboard__ (square for each type)
            - show:
                - sensors readings
                - states of actuators and their actions
                - time
                - weather
            - each square has buttons:
                - hide
                - settings
                    - which data to show
                    - thresholds, warnings
                - drag handle/unlock/pin
                - resize
        - __Charts__
            - graphs
                - one or multiple graphs occupying whole screen
                - choose which data to show on which graph
                  - multiple lines on one graph
                  - data vs data (X: temperature, Y:wind speed)
                  - add datasets to X or Y axes
                - add markers, notes
        - __Settings__
            - USER
              - language
              - color theme
              - layout
              - homepage
            - DATA
              - units of measure (C / F) etc
                - DB stores only metric, UI converts them
                - use standard markup like HomeAssistant (https://www.home-assistant.io/blog/2015/10/11/measure-temperature-with-esp8266-and-report-to-mqtt/)
              - location
              - refresh rates (sensors, internet services)
              - database granularity / age
              - notifications
              - Server comms
            - DEVICES
              - **add/change Device**
                - device name (new or dropdown)
                - select interface (dropdown)
                  - USB
                    - port?
                  - WIFI
                    - ip address
                  - ETHERNET
                    - ip address
                - Device type (dropdown)
                  - arduino (dropdown)
                  - NodeMCU
                  - stm32
                  - raspberry pi
              - **add/change SENSOR**
                - connected to device name (dropdown of existing)
                - Name(new or dropdown)
                - type of sensor
                  - temp
                  - humid
                  - ...
                - interface (pins)
                  - Analog
                  - digital
                  - SPI
                  - address
                  - I2C
                    - address
                  - onewire
                    - address
              - general setup
        - __Log__
            - all events, actions (live and historical)
                - select and color code by category
                    - User actions
                        - actuators
                        - refresh request
                        - setting changed
                        - database manipulations (note added, data cleared)
                    - sensors
                    - internet comms
                    - server comms
                    - database access r, w, mod
            - store log on server hdd and cloud
            - sort by..
            - show/hide data groups
        - __Future__
            - graphs + notes
                - choose how distant the future
                - choose which data to display
                - choose scenario (worst case, avg, based on time period A->B)
                - compare past events with predictions and give feedback? automatic?
        - __Weather__
          - charts
          - dashboards
          - gardening info
        - __TODAY__
          - daily report
            - water consumed/water gained
            - energy gathered
            - min max temp
            - sunrise sunset
            - hours of rain
            - outlying readings


- each sensor panel or chart should have a (go fullscreen) button. if then clicked again, it returns to normal
- Ifvisible.js: Crossbrowser & lightweight way to check if user is looking at the page or interacting with it.



## ICONS

<i class="fas fa-cogs"></i>
<i class="fas fa-chart-line"></i>
<i class="fas fa-tachometer-alt"></i>
<i class="fas fa-list-ol"></i>

<i class="fas fa-user-cog"></i>
<i class="fas fa-bars"></i>
<i class="fas fa-tasks"></i>
<i class="fas fa-cloud"></i>
<i class="fas fa-temperature-low"></i>
<i class="fas fa-sun"></i>
<i class="fas fa-water"></i>
<i class="fas fa-wifi"></i>
<i class="fas fa-network-wired"></i>
<i class="fas fa-ethernet"></i>
<i class="fas fa-tint"></i>
<i class="fas fa-history"></i>
<i class="fas fa-clock"></i>
<i class="fas fa-calendar-alt"></i>
<i class="fas fa-user-tie"></i>
<i class="fas fa-user-circle"></i>
<i class="fas fa-sort-amount-up"></i>
<i class="fas fa-solar-panel"></i>
<i class="fas fa-car-battery"></i>
<i class="fas fa-power-off"></i>
<i class="fas fa-filter"></i>
<i class="fas fa-save"></i>
<i class="fas fa-eye"></i>
<i class="fas fa-eye-slash"></i>
<i class="fas fa-ruler"></i>
<i class="fas fa-palette"></i>
<i class="fas fa-poop"></i>
<i class="fas fa-poo"></i>
<i class="fas fa-lightbulb"></i>
<i class="fas fa-award"></i>
<i class="fas fa-bullhorn"></i>
<i class="fas fa-flag-checkered"></i>
<i class="fas fa-info"></i>
<i class="fas fa-search"></i>
<i class="fas fa-thumbs-up"></i>
<i class="fas fa-thumbs-down"></i>
<i class="fas fa-map-marker-alt"></i>
<i class="fas fa-exclamation"></i>
<i class="fas fa-info-circle"></i>
<i class="fas fa-check-circle"></i>
<i class="fas fa-thumbtack"></i>