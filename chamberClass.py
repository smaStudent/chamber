# from errors import ErrorDict        # to bedzie potrzebne do obslugi bledow
from functions import *


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
        self.periodOfRead = 10  # seconds
        self.amountOfDataInTabs = 10
        self.counter = 0
        self.tempFile = 'tempData.txt'
        self.humiFile = 'humiData.txt'

        # commands for having a response
        self.resetCommand = 'SRQ?\r\n'
        self.tempAsk = 'TEMP?\r\n'
        self.humiAsk = 'HUMI?\r\n'
        self.heaterAsk = '%?\r\n'
        self.condInside = 'MON?\r\n'
        # self.lastString = '\r\n'    # it has to be in every single message

        # check if we have open connection

        self.tempTab = []
        self.humiTab = []

        self.ser.open()

        if self.ser.isOpen():
            print("Connected successfully")
        else:
            print("ERROR, can not connect with chamber!")

    def update(self):
        period = datetime.datetime.now()
        if period.second % self.periodOfRead == 0:  # if periodOfRead seconds passed, we do what is inside the if
            # statement
            self.timeInIteration = datetime.datetime.now()
            self.tempTab.append(self.tempData())
            self.humiTab.append(self.humiData())
            if self.amountOfDataInTabs == self.counter:
                try:
                    saveToFile(self.tempFile, self.tempTab)     # we passed string with name and tab contains data from chamber
                    saveToFile(self.humiFile, self.humiTab)     # same here
                    self.tempTab = []                           # clear the tab if we succeed
                    self.humiTab = []                           # same here
                except:
                    print("Error in saving the file")

                self.counter = 0

            self.counter = self.counter+1

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
        print("TEMP: ", self.timeInIteration.year, self.timeInIteration.month, self.timeInIteration.day, self.timeInIteration.hour, self.timeInIteration.minute, self.timeInIteration.second, PV, SP, lowVal, maxVal)
        return self.timeInIteration.year, self.timeInIteration.month, self.timeInIteration.day, self.timeInIteration.hour, self.timeInIteration.minute, self.timeInIteration.second, PV, SP, lowVal, maxVal

    def humiData(self):
        PV, SP, lowVal, maxVal = changeAnsForTable(sendAndReceive(self.ser, self.humiAsk))
        print("HUMI: ", self.timeInIteration.year, self.timeInIteration.month, self.timeInIteration.day, self.timeInIteration.hour, self.timeInIteration.minute, self.timeInIteration.second, PV, SP, lowVal, maxVal)
        return self.timeInIteration.year, self.timeInIteration.month, self.timeInIteration.day, self.timeInIteration.hour, self.timeInIteration.minute, self.timeInIteration.second, PV, SP, lowVal, maxVal
