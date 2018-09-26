import serial
import time
#from errors import ErrorDict        # to bedzie potrzebne do obslugi bledow
import datetime


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
        #self.lastString = '\r\n'    # it has to be in every single message

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



        # check if we have open connection

        self.tempTab = []
        self.humiTab = []

        if self.ser.isOpen():
            print("Connected successfully")
        else:
            print("ERROR, can not connect with chamber!")

    def update(self):
        self.timeInIteration = datetime.datetime.now()
        self.getNewVal()

        if self.iteration == 50:

        self.iteration = self.iteration + 1



    ####################################
    ######### helpful function #########
    ####################################

    def sendAndReceive(self, serialObject, message):
        serialObject.write(bytearray(message, 'utf-8'))
        time.sleep(0.2)
        ans = serialObject.readline()
        return ans

    def dealWithTemp(self):
        global highLim, lowLim, tempSV, tempPV
        tempStr = str()
        whichIter = 0
        ansTemp = self.sendAndReceive(self.ser, self.tempAsk)
        # here check if we didn't get an error

        for c in ansTemp:
            if c == ',':
                whichIter = whichIter + 1
                tempStr = str()
            else:
                tempStr = tempStr + c

            tempInt = int(tempStr)

            if whichIter == 0:
                tempPV = tempInt
            if whichIter == 1:
                tempSV = tempInt
            if whichIter == 2:
                highLim = tempInt
            if whichIter == 3:
                lowLim = tempInt

        self.tempTab[self.iteration,0] = self.timeInIteration.year
        self.tempTab[self.iteration,1] = self.timeInIteration.month
        self.tempTab[self.iteration,2] = self.timeInIteration.day
        self.tempTab[self.iteration,3] = self.timeInIteration.hour
        self.tempTab[self.iteration,4] = self.timeInIteration.minute
        self.tempTab[self.iteration,5] = self.timeInIteration.second
        self.tempTab[self.iteration,6] = tempPV
        self.tempTab[self.iteration,7] = tempSV
        self.tempTab[self.iteration,8] = highLim
        self.tempTab[self.iteration,9] = lowLim

    def dealWithHumi(self):
        global highLim, lowLim, humiSV, humiPV
        tempStr = str()
        whichIter = 0
        ansHumi = self.sendAndReceive(self.ser, self.humiAsk)
        # here check if we didn't get an error

        for c in ansHumi:
            if c == ',':
                whichIter = whichIter + 1
                tempStr = str()
            else:
                tempStr = tempStr + c

            tempInt = int(tempStr)

            if whichIter == 0:
                humiPV = tempInt
            if whichIter == 1:
                humiSV = tempInt
            if whichIter == 2:
                highLim = tempInt
            if whichIter == 3:
                lowLim = tempInt

        self.humiTab[self.iteration,0] = self.timeInIteration.year
        self.humiTab[self.iteration,1] = self.timeInIteration.month
        self.humiTab[self.iteration,2] = self.timeInIteration.day
        self.humiTab[self.iteration,3] = self.timeInIteration.hour
        self.humiTab[self.iteration,4] = self.timeInIteration.minute
        self.humiTab[self.iteration,5] = self.timeInIteration.second
        self.humiTab[self.iteration,6] = humiPV
        self.humiTab[self.iteration,7] = humiSV
        self.humiTab[self.iteration,8] = highLim
        self.humiTab[self.iteration,9] = lowLim


    def getNewVal(self):
        self.dealWithTemp()
        self.dealWithHumi()

    def saveTableToFile(self, obj, dictionary):
        for key,val in dictionary:
            obj.write(val+'\n')
        obj.close()

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
