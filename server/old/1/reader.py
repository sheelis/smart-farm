import json

from lib import arduino_serial

class Nano():
    temperature = 420
    
    #  def getReading(self):
    #     self.temperature += 1
    #     data_type = "reading"
    #     devID = "greenhouse1"
    #     readingID1 = "temp1"
    #     readingID2 = "humidity"
    #     # return '{"temp1":'+ str(self.temperature)+'}'
    #     jsonstring = '{"'+data_type+'": [{"'+devID+'": [{"name":"'+readingID1+'", "value": '+ str(self.temperature)+'}, {"name":"'+readingID2+'", "value": '+ str(self.temperature-53)+'}]}]}'
    #     return jsonstring
        
    def getReading(self):
        nanos = arduino_serial.find("")
        devID = nanos[0][1]
        self.temperature = nanos[0][0].get_reading()


        data_type = "reading"
        # devID = "greenhouse1"
        readingID1 = "temp1"
        readingID2 = "humidity"
        jsonstring = '{"'+data_type+'": [{"'+str(devID)+'": [{"name":"'+readingID1+'", "value": '+ str(self.temperature)+'}, {"name":"'+readingID2+'", "value": 420}]}]}'
        return jsonstring

if __name__ == "__main__":
    import json
    x = Nano.getReading(Nano)
    print( x )