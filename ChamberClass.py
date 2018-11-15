# from errors import ErrorDict        # to bedzie potrzebne do obslugi bledow
from functions import *
import serial
import DataStruct
import datetime
import time


class Chamber:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        print("Let's start")
        # setting up serial connection
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

        # commands for having a response
        self.resetCommand = 'SRQ?\r\n'
        self.tempAsk = 'TEMP?\r\n'
        self.humiAsk = 'HUMI?\r\n'
        self.heaterAsk = '%?\r\n'
        self.condInside = 'MON?\r\n'
        
        # consts that we need 
        self.periodOfRead = 10
        self.sizeOfTheTable = 5
        
        try:
            self.ser.open()                         # openning the port
        except serial.SerialException:
            print(serial.SerialException, "unable to open the port")
            counter = 1
            while self.ser.isOpen() and counter <100:
                self.ser.open()
                time.sleep(5)
                counter += 1

        # tables for data
        self.tempDataTable = []
        self.humiDataTable = []
                
        


    def __del__(self):
        self.ser.close()
        print("Destruktor zadzialal")
        # saveToFile(self.tempFile, self.tempTab)
        # saveToFile(self.humiFile, self.humiTab)
        # here we can add feature like switch on red LED
        # print("We end work for now, you have your data in files")

    def update(self):
        timeInUpdate = datetime.datetime.now()
        
        if timeInUpdate.second % self.periodOfRead == 0:
            self.updateTemp(timeInUpdate)
            self.updateHumi(timeInUpdate)

        elif self.doWeNeedPushData():
            saveTabToFile("tempDataFile.txt", self.tempDataTable)
            saveTabToFile("humiDataFile.txt", self.humiDataTable)

            saveTabMySQLTemp('mysql01.saxon.beep.pl', 'sub_saxon', 'passwd', 'test_database', self.tempDataTable)
            saveTabMySQLHumi('mysql01.saxon.beep.pl', 'sub_saxon', 'passwd', 'test_database', self.humiDataTable)

            self.tempDataTable = []
            self.humiDataTable = []

        time.sleep(1)


    ####################################
    ######### helpful function #########
    ####################################

    def updateTemp(self, currentTime):
        print("Robimy teraz w ChamberClass, tempData")
        PV, SP, lowLv, maxLv = changeAnsForTable(sendAndReceive(self.ser, self.tempAsk))
        self.tempDataTable.append(DataStruct.DataStruct(currentTime, PV, SP, lowLv, maxLv))


    def getTemp(self, whichOne = None):
        print("Robimy teraz w ChamberClass, getData")
        if whichOne != "all":
            return self.tempDataTable[-1]
        else:
            return self.tempDataTable


    def updateHumi(self, currentTime):
        print("Robimy teraz w ChamberClass, humiData")
        PV, SP, lowLv, maxLv = changeAnsForTable(sendAndReceive(self.ser, self.humiAsk))
        self.humiDataTable.append(DataStruct.DataStruct(currentTime, PV, SP, lowLv, maxLv))


    def getHumi(self, whichOne = None):
        print("Robimy teraz w ChamberClass, getHumi")
        if whichOne != "all":
            return self.humiDataTable[-1]
        else:
            return self.humiDataTable
        
        
    def doWeNeedPushData(self):
        if self.tempDataTable.__len__() >= self.sizeOfTheTable and self.tempDataTable.__len__() >= self.sizeOfTheTable:
            return True
        else:
            return False
        
#############################################################################
###########################   OLD CODE  #####################################
#############################################################################


# def showDate(self):
#     print(self.timeInIteration)
#
# def showTemp(self):
#     if self.ser.isOpen():
#         print(sendAndReceive(self.ser, self.tempAsk))
#         return sendAndReceive(self.ser, self.tempAsk)
#     else:
#         print("Lost connection with chamber")
#
# def showHumi(self):
#     if self.ser.isOpen():
#         print(sendAndReceive(self.ser, self.humiAsk))
#         return sendAndReceive(self.ser, self.humiAsk)
#     else:
#         print("Lost connection with chamber")




# 1
