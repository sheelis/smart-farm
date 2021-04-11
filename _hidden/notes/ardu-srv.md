# arduino - server comms

# arduino to server

- new readings (only when there is a change)
  - jsonstring = '{"'+data_type+'": [{"'+devID+'": [{"'+readingID+'": '+ str(self.temperature)+'}]}]}'
- status of command execution
- current status (regular ping)
- my ID

# server to arduino

- motion commands
  - non-blocking
- ping request
- ID yourself