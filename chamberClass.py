import serial
import time
from errors import ErrorDict        # to bedzie potrzebne do obslugi bledow
import datetime


class Chamber:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        self.ser = serial.Serial()

        self.ser.port = port
        self.ser.baudrate = baudrate
        self.ser.polarity = None
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.timeout = 1
        self.ser.write_timeout = 2
        self.ser.parity = serial.PARITY_NONE
        self.ser.dsrdtr = True
        self.periodOfRead = 20  # seconds

        # commands for having a response
        self.resetCommand = 'SRQ?\r\n'
        self.tempAsk = 'TEMP?\r\n'
        self.humiAsk = 'HUMI?\r\n'
        self.heaterAsk = '%?\r\n'
        self.condInside = 'MON?\r\n'
        #self.lastString = '\r\n'    # it has to be in every single message

        self.tempTable = {'NAME': 'TEMP',
                          'TIME': None,
                          'PV': None,
                          'SP': None,
                          'MIN': None,
                          'MAX': None}

        self.humiTable = {'NAME': 'HUMI',
                          'TIME': None,
                          'PV': None,
                          'SV': None,
                          'MIN': None,
                          'MAX': None}

        self.heaterTable ={'NAME': 'HEATER_OUTPUT',
                          'TIME': None,
                          'NUMBER_OF_HEATERS': None,
                          'HEATER_OUTPUT': None,
                          'HUMIDIFYING_HEAT_OUT': None}

        self.condInsideTable = {'NAME': 'CURRENT_PROGRAM_PARAMETERS',
                          'TIME': None,
                          'No. of current program': None,
                          'No. of current step': None,
                          'TARGET_TEMP': None,
                          'TARGET_HUMI': None,
                          'EXPOSURE_TIME_REMAINING': None,
                          'NUMBER_OF_REPEAT': None,
                          'CYCLES_REMAINING': None}

        # check if we have open connection
        if self.ser.isOpen():
            print("Connected successfully")
        else:
            print("ERROR, can not connect with chamber!")

    def getNewVal(self):












    ####################################
    ######### helpful function #########
    ####################################
    def checkIfNotError(self, ans):
        if
    def dealWithTemp(self):
        tempStr = str()
        whichIter = 0
        ansTemp = self.sendAndReceive(self.ser, self.tempAsk)
        # here check if we didn't get an error

        for c in ansTemp:
            if s == ',':
                whichIter = whichIter + 1


                }
            else:








        simpleStr = '2, 56.2, 38.9'
        tempStr = str()
        for s in simpleStr:
            if s == ',':
                print(tempStr)
                tempStr = str()
            else:
                tempStr = tempStr + s



    def dealWithHumi(self):
        ansHumi = self.sendAndReceive(self.ser, self.humiAsk)


    def dealWithHeaterOutput(self):
        ansHeterOutput = self.sendAndReceive(self.ser, self.heaterAsk)


    def dealWithCondInside(self):
        ansCondInside = self.sendAndReceive(self.ser, self.condInside)

    def sendAndReceive(self, serialObject, message):
        serialObject.write(bytearray(message, 'utf-8'))
        time.sleep(0.2)
        ans = serialObject.readline()
        return ans


# def sendAndReceive(serialObject, message):
#     serialObject.write(bytearray(message, 'utf-8'))
#     time.sleep(0.2)
#     ans = serialObject.readline()
#     return ans
#
# def sendAndReadFirst(serialObject):
#     serialObject.write(b'SRQ?\r\n')
#     time.sleep(0.2)
#     ans = serialObject.readline()
#     return ans
#
#
# def sendAndReadTemp(serialObject):
#     serialObject.write(b'TEMP?\r\n')
#     time.sleep(0.2)
#     ans = serialObject.readline()
#     return ans
#
