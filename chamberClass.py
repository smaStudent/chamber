import serial
import time
# from errors import ErrorDict        # to bedzie potrzebne do obslugi bledow
import datetime
from functions import *
import numpy as np


class Chamber:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        self.timeInIteration = None
        self.iteration = 0

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
        # self.lastString = '\r\n'    # it has to be in every single message

        # check if we have open connection

        # self.tempTab = np.array(50, 50, np.int32)
        # self.humiTab = np.array()

        self.ser.open()

        if self.ser.isOpen():
            print("Connected successfully")
        else:
            print("ERROR, can not connect with chamber!")

    def update(self):
        period = datetime.datetime.now()
        if period.second % 1 == 0:  # if 20 seconds passed, we do what is inside the if statement
            self.timeInIteration = datetime.datetime.now()


    ####################################
    ######### helpful function #########
    ####################################

    def showDate(self):
        print(self.timeInIteration)

    def showTemp(self):
        print(sendAndReceive(self.ser, self.tempAsk))
        return sendAndReceive(self.ser, self.tempAsk)

    def showHumi(self):
        print(sendAndReceive(self.ser, self.humiAsk))
        return sendAndReceive(self.ser, self.humiAsk)

    def tempData(self):
        PV, SP, lowVal, maxVal = changeAnsForTable(sendAndReceive(self.ser, self.tempAsk))
        return self.timeInIteration.year, self.timeInIteration.month, self.timeInIteration.day, self.timeInIteration.hour, self.timeInIteration.minute, self.timeInIteration.second, PV, SP, lowVal, maxVal

    def humiData(self):
        PV, SP, lowVal, maxVal = changeAnsForTable(sendAndReceive(self.ser, self.humiAsk))
        return self.timeInIteration.year, self.timeInIteration.month, self.timeInIteration.day, self.timeInIteration.hour, self.timeInIteration.minute, self.timeInIteration.second, PV, SP, lowVal, maxVal

################### OLD CODE ###############################


# def checkIfNotError(self, ans):
#     #tutaj cos trzeba dac

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


#    def dealWithHeaterOutput(self):
#         global humiHeterOut, heaterOutput, tempNum
#         ansHeterOutput = self.sendAndReceive(self.ser, self.heaterAsk)
#         tempStr = str()
#         whichIter = 0
#         # here check if we didn't get an error
#
#         for c in ansHeterOutput:
#             if c == ',':
#                 whichIter = whichIter + 1
#                 tempStr = str()
#             else:
#                 tempStr = tempStr + c
#
#             tempInt = int(tempStr)
#
#             if whichIter == 0:
#                 tempNum = tempInt
#             if whichIter == 1:
#                 heaterOutput = tempInt
#             if whichIter == 2:
#                 humiHeterOut = tempInt
#
#         self.heaterTable = {'NAME': 'HEATER_OUTPUT', 'TIME': self.timeInIteration, 'NUMBER_OF_HEATERS': tempNum, 'HEATER_OUTPUT': heaterOutput, 'HUMIDIFYING_HEAT_OUT': humiHeterOut}


# self.tempTable = {'NAME': 'TEMP',
#                   'TIME': None,
#                   'PV': None,
#                   'SP': None,
#                   'MIN': None,
#                   'MAX': None}
#
# self.humiTable = {'NAME': 'HUMI',
#                   'TIME': None,
#                   'PV': None,
#                   'SV': None,
#                   'MIN': None,
#                   'MAX': None}
#
# self.heaterTable ={'NAME': 'HEATER_OUTPUT',
#                   'TIME': None,
#                   'NUMBER_OF_HEATERS': None,
#                   'HEATER_OUTPUT': None,
#                   'HUMIDIFYING_HEAT_OUT': None}
