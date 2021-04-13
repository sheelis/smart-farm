""" This module handles all communication with an arduino 
USAGE:
from lib import arduino_serial          # import this library
allarduinos = arduino_serial.find("")   # find all connected arduinos
"""

import time
import serial
import serial.tools.list_ports

ARDU_ID = "CH340"       # string that identifies arduino in the serial ports list
BAUDRATE = 9600         # default baudrate
T_OUT = 4               # default timeout
codeID = "SERIAL:\t"   # name of this code as appears in console

def find(needed_id):
    """
    This function finds all or a specific arduino by it's ID
    Returns a list containing [handle, ID]
    """
    found_arduinos = []                                                         # create a list for storing found arduinos
    ports = list(serial.tools.list_ports.comports())                            # read all communications ports
    for portinfo in ports:
        if ARDU_ID in portinfo[1]:                                              # if its an arduino (ardu_ID present in the string)
            # should check for other IDs too
            ardu = Arduino(portinfo, BAUDRATE, T_OUT)                           # connect to verify
            # should try other baudrates too
            time.sleep(2)
            firmware_id_version = ardu.get_version()                            # request ID and vesion
            if needed_id != "":                                                 # if looking for 1 arduino
                print(codeID+"Looking for \t" + needed_id)
                if needed_id in firmware_id_version:                            # if nedded arduino found
                    found_arduinos.append([ardu.serial, firmware_id_version])   # add to list
                    break # stop looking
            else:
                found_arduinos.append([ardu, firmware_id_version])              # add to list
    # report findings:
    print("")
    if len(found_arduinos) < 1:
        print(codeID+"---- No arduinos found!")
    else:
        print(codeID+"---- Found " + str(len(found_arduinos)) + " arduino(s):")
        for found_arduino in found_arduinos:
            print("\t | " + str(found_arduino[0].portinfo) + "\t" + str(found_arduino[1]))
    print("")
    return found_arduinos


class Arduino():
    """ This Class defines an arduino device. """
    def __init__(self, portinfo, baudr, time_out):
        """
        Initializes the serial connection to the Arduino board
        """
        self.portinfo = portinfo
        self.serial = serial.Serial(portinfo[0], baudr, timeout=time_out)
        # print("Connected to:" + self.serial.port)
        print(codeID+portinfo[0]+"\t Connected!")

    def clear_input(self):
        """ Clear serial input buffer so fresh readings can be obtained. """
        # print("clear_input")
        self.serial.flushInput() #for python 2
        # self.serial.reset_input_buffer() #for python 3
        # self.serial.flush()

    def clear_output(self):
        """ Clear serial output buffer so fresh commands can be sent to it. """
        # print("clear_output")
        self.serial.flushOutput()
        # self.serial.reset_output_buffer() #for python 3
        #self.serial.flush()

    def get_version(self):
        """ Sends "version" to arduino and gets response """
        print(codeID+self.serial.port+"\t requesting version..")
        self.clear_input()
        # self.clear_output()
        self.send('version')
        firmware_id_version = self.get_reading()
        return firmware_id_version

    def send(self, command):
        """ send a string to arduino over serial """
        self.serial.write(str(command+"\n").encode())

    def get_reading(self):
        """ Gets readings from arduino (reads a line) """
        print(codeID+self.serial.port+"\t reading..")
        #self.clear_input()
        # time.sleep(1)
        input_string = self.serial.readline().decode("utf-8").strip()
        # try:
        #     input_string.decode("utf-8").strip() # Find what the nano says
        # except ValueError:
        #     print('invalid reading, got {}'.format(input_string))
        return input_string

    def close(self):
        """
        To ensure we are properly closing our connection to the
        Arduino device.
        """
        self.serial.close()
        # print('Connection to '+ self.serial.port + ' closed')
        print(codeID+self.serial.port+'Connection closed')
