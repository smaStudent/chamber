import serial
import time
# from errors import ErrorDict        # to bedzie potrzebne do obslugi bledow
import datetime
from functions import saveTableToFile
from functions import sendAndReceive
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

        #self.tempTab = np.array(50, 50, np.int32)
        #self.humiTab = np.array()

        self.ser.open()

        if self.ser.isOpen():
            print("Connected successfully")
        else:
            print("ERROR, can not connect with chamber!")

    def update(self):
        period = datetime.datetime.now()
        if period.second % 1 == 0:  # if 20 seconds passed, we do what is inside the if statement
            self.timeInIteration = datetime.datetime.now()
            #self.getNewVal()

            if self.iteration == 1:
                # here we've to put function for moving data from tables to files
                tempFile = open('tempData.txt', 'a')
                humiFile = open('humiData.txt', 'a')

                saveTableToFile(tempFile, self.dealWithTemp())
                saveTableToFile(humiFile, self.dealWithHumi())
                print("Dane przeniesione do pliku ")
                self.iteration = 0
                self.tempTab = 0
                self.humiTab = 0

            self.iteration = self.iteration + 1
            time.sleep(1)  # we wait 1 sec to avoid taking 2nd time the same values
            print("po sleep, nowa iteracja")

    ####################################
    ######### helpful function #########
    ####################################

    def showTemp(self):
        print(sendAndReceive(self.ser, self.tempAsk))

    def dealWithTemp(self):
        global highLim, lowLim, tempSV, tempPV
        highLim = str()
        lowLim = str()
        tempSV = str()
        tempPV = str()
        tempStr = str()
        whichIter = 0
        ansTemp = sendAndReceive(self.ser, self.tempAsk)
        print("Odpowiedz z sendAndReceive: ", ansTemp)
        # here check if we didn't get an error

        for c in ansTemp:
            if c == ',':
                whichIter = whichIter + 1
                tempStr = str()
            else:
                tempStr = tempStr + str(c)

            tempInt = int(tempStr)

            if whichIter == 0:
                tempPV = tempInt
            if whichIter == 1:
                tempSV = tempInt
            if whichIter == 2:
                highLim = tempInt
            if whichIter == 3:
                lowLim = tempInt


        print("temperetura, sciagnieta")
        print("temperatura to: ", tempPV)
        return [str(self.timeInIteration.year), str(self.timeInIteration.month), str(self.timeInIteration.day),
                str(self.timeInIteration.hour), str(self.timeInIteration.minute), str(self.timeInIteration.second),
                str(tempPV), str(tempSV), str(highLim), str(lowLim)]

        # self.tempTab[self.iteration, 0] = str(self.timeInIteration.year)
        # self.tempTab[self.iteration, 1] = str(self.timeInIteration.month)
        # self.tempTab[self.iteration, 2] = str(self.timeInIteration.day)
        # self.tempTab[self.iteration, 3] = str(self.timeInIteration.hour)
        # self.tempTab[self.iteration, 4] = str(self.timeInIteration.minute)
        # self.tempTab[self.iteration, 5] = str(self.timeInIteration.second)
        # self.tempTab[self.iteration, 6] = str(tempPV)
        # self.tempTab[self.iteration, 7] = str(tempSV)
        # self.tempTab[self.iteration, 8] = str(highLim)
        # self.tempTab[self.iteration, 9] = str(lowLim)
        # print("temperetura, sciagnieta")

    def dealWithHumi(self):
        global highLim, lowLim, humiSV, humiPV
        highLim = str()
        lowLim = str()
        humiPV = str()
        humiSV = str()
        tempStr = str()
        whichIter = 0
        ansHumi = sendAndReceive(self.ser, self.humiAsk)
        # here check if we didn't get an error
        print("Odpowiedz z sendAndReceive: ", ansHumi)

        for c in ansHumi:
            if c == ',':
                whichIter = whichIter + 1
                tempStr = str()
            else:
                tempStr = tempStr + str(c)

            tempInt = int(tempStr)

            if whichIter == 0:
                humiPV = tempInt
            if whichIter == 1:
                humiSV = tempInt
            if whichIter == 2:
                highLim = tempInt
            if whichIter == 3:
                lowLim = tempInt

        print("wilgotnosc sciagnieta")
        print("wilgotnosc to: ", humiPV)
        return [str(self.timeInIteration.year), str(self.timeInIteration.month), str(self.timeInIteration.day),
                str(self.timeInIteration.hour), str(self.timeInIteration.minute), str(self.timeInIteration.second),
                str(humiPV), str(humiSV), str(highLim), str(lowLim)]
        #
        # self.humiTab[self.iteration, 0] = str(self.timeInIteration.year)
        # self.humiTab[self.iteration, 1] = str(self.timeInIteration.month)
        # self.humiTab[self.iteration, 2] = str(self.timeInIteration.day)
        # self.humiTab[self.iteration, 3] = str(self.timeInIteration.hour)
        # self.humiTab[self.iteration, 4] = str(self.timeInIteration.minute)
        # self.humiTab[self.iteration, 5] = str(self.timeInIteration.second)
        # self.humiTab[self.iteration, 6] = str(humiPV)
        # self.humiTab[self.iteration, 7] = str(humiSV)
        # self.humiTab[self.iteration, 8] = str(highLim)
        # self.humiTab[self.iteration, 9] = str(lowLim)
        # print("wilgotnosc sciagnieta")

    def getNewVal(self):
        self.dealWithTemp()
        self.dealWithHumi()
        print("getNewVal, dziala chyba")
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
