# server - client communications

all comms use json

- type of info:
  - subsection:
    - key: value


[{"type": {
    "subsection": [{
        "key": 'value', 
        "key":3
        }]
    }
}]


## server sends to client:

- sensor readings
  - jsonstring = '{"'+data_type+'": [{"'+devID+'": [{"'+readingID+'": '+ str(self.temperature)+'}]}]}'
    - {"reading": [{"tent1": [{"temp1": 421}]}]}
- notifications
  - danger
  - predictions
- setting
  - refresh intervals
  - system status
  - user preferences

## client sends to server:

- device commands
  - turn on light
  - refresh readings
- UI settings
  - change interval
  - change sensor appearance (chart, bar)
- DB settings
  - add new sensor
  - change timer
  - schedule a task