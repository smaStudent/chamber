# from errors import ErrorDict        # to bedzie potrzebne do obslugi bledow
from functions import *
import serial
import DataStruct
import datetime
import time


class Chamber:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600, periodOfRead=20, sizeOfTheTable=100):
        # just in case if someone will plug our adapter into bad port (designed for raspberry pi with 3 ports
        portTab = ['/dev/ttyUSB1', '/dev/ttyUSB2', '/dev/ttyUSB3']

        # print("Let's start")
        # setting up serial connection
        self.ser = serial.Serial()
        try:
            self.ser.port = port
        except:
            for i in portTab:
                try:
                    self.ser.port = i
                    break
                except:
                    continue
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
        self.periodOfRead = periodOfRead
        self.sizeOfTheTable = sizeOfTheTable

        try:
            self.ser.open()  # openning the port
        except serial.SerialException as e:
            print(e, "unable to open the port")
            counter = 1
            saveProblem(datetime.datetime.now(), comment="Problem in __init__() while create chamber instance")
            while self.ser.isOpen() and counter < 100:
                self.ser.open()
                time.sleep(5)
                counter += 1

        # tables for data
        self.tempDataTable = []
        self.humiDataTable = []
        print("Udało się cały konstruktor")
        print(self.ser.port)
        print("\n")

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
            try:
                self.updateTemp(timeInUpdate)
                self.updateHumi(timeInUpdate)
            except:
                saveProblem(timeInUpdate, comment="Nie udało się w funkcji update self.updateTemp/Humi")

            # print(self.getTemp().__str__())
            # print(self.getHumi().__str__())

        elif self.doWeNeedPushData():
            # saveTabToFile("tempDataFile.txt", self.tempDataTable)
            # saveTabToFile("humiDataFile.txt", self.humiDataTable)
            saveTabMySQLTemp('', '', '', 'test_database',
                             self.tempDataTable)  # this is already protected in the functon implementation and just in case saved in the file
            saveTabMySQLHumi('', '', '', 'test_database',
                             self.humiDataTable)  # this is already protected in the functon implementation and just in case saved in the file

            self.tempDataTable = []
            self.humiDataTable = []

        time.sleep(1)

    ####################################
    ######### helpful function #########
    ####################################

    def instantPushData(self):
        saveTabMySQLTemp('', '', '', 'test_database',
                         self.tempDataTable)
        saveTabMySQLHumi('', '', '', 'test_database',
                         self.humiDataTable)


    def updateTemp(self, currentTime):
        # print("Robimy teraz w ChamberClass, tempData")
        try:
            PV, SP, lowLv, maxLv = changeAnsForTable(sendAndReceive(self.ser, self.tempAsk))
            self.tempDataTable.append(DataStruct.DataStruct(currentTime, PV, SP, lowLv, maxLv))
        except:
            raise

    def getTemp(self, whichOne=None):
        # print("Robimy teraz w ChamberClass, getData")
        if whichOne != "all":
            return self.tempDataTable[-1]
        else:
            return self.tempDataTable

    def updateHumi(self, currentTime):
        # print("Robimy teraz w ChamberClass, humiData")
        try:
            PV, SP, lowLv, maxLv = changeAnsForTable(sendAndReceive(self.ser, self.humiAsk))
            self.humiDataTable.append(DataStruct.DataStruct(currentTime, PV, SP, lowLv, maxLv))
        except:
            raise

    def getHumi(self, whichOne=None):
        # print("Robimy teraz w ChamberClass, getHumi")
        if whichOne != "all":
            return self.humiDataTable[-1]
        else:
            return self.humiDataTable

    def doWeNeedPushData(self):
        if self.tempDataTable.__len__() >= self.sizeOfTheTable and self.tempDataTable.__len__() >= self.sizeOfTheTable:
            return True
        else:
            return False

    def checkAlarm(self):
        alarm = sendAndReceive(self.ser, 'ALARM?\r\n')

        if alarm != 0:
            print(alarm)
            return alarm
        else:
            return 0

    ###########################
    ######## old code #########
    ###########################

    def checkAllParameters(self):
        # PRGM                    Controls the current program.

        print("odp na ROM? \t", sendAndReceive(self.ser, 'ROM?\r\n'))
        print("odp na SRQ?\t", sendAndReceive(self.ser, 'RUN PRGM SRQ?\r\n'))
        print("odp na MASK?\t", sendAndReceive(self.ser, 'MASK?\r\n'))
        print("odp na ALARM?\t", sendAndReceive(self.ser, 'ALARM?\r\n'))

        print("odp na KEYPROTECT? \t", sendAndReceive(self.ser, 'KEYPROTECT?\r\n'))
        print("odp na TYPE?\t", sendAndReceive(self.ser, 'TYPE?\r\n'))
        print("odp na MODE?\t", sendAndReceive(self.ser, 'MODE?\r\n'))
        print("odp na MON?\t", sendAndReceive(self.ser, 'MON?\r\n'))

        print("odp na SET?\t", sendAndReceive(self.ser, 'SET?\r\n'))
        print("odp na REF?\t", sendAndReceive(self.ser, 'REF?\r\n'))
        print("odp na PRGM MON?\t", sendAndReceive(self.ser, 'PRGM MON?\r\n'))
        print("odp na PRGM DATA?\t", sendAndReceive(self.ser, 'PRGM DATA?\r\n'))

        print("odp na RUN PRGM MON?\t", sendAndReceive(self.ser, 'RUN PRGM MON?\r\n'))
        print("odp na RUN PRGM?\t", sendAndReceive(self.ser, 'RUN PRGM?\r\n'))
