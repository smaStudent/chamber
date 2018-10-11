# from errors import ErrorDict        # to bedzie potrzebne do obslugi bledow
from functions import *
import serial


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
        self.amountOfDataInTabs = 100
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

    def __del__(self):
        self.ser.close()
        saveToFile(self.tempFile, self.tempTab)
        saveToFile(self.humiFile, self.humiTab)
        # here we can add feature like switch on red LED
        print("We end work for now, you have your data in files")

    def update(self):
        period = datetime.datetime.now()
        if period.second % self.periodOfRead == 0:  # if periodOfRead seconds passed, we do what is inside the if
            # statement
            self.checkIfItConnected()
            self.timeInIteration = datetime.datetime.now()
            print("Iteracja nr: ", self.counter)
            self.tempTab.append(self.tempData())
            self.humiTab.append(self.humiData())
            if self.amountOfDataInTabs == self.counter:
                try:
                    saveToFile(self.tempFile,
                               self.tempTab)  # we passed string with name and tab contains data from chamber
                    saveToFile(self.humiFile, self.humiTab)  # same here
                    self.tempTab = []  # clear the tab if we succeed
                    self.humiTab = []  # same here
                except:
                    print("Error in saving the file")

                self.counter = 0

            time.sleep(0.99)
            self.counter = self.counter + 1

    ####################################
    ######### helpful function #########
    ####################################

    def showDate(self):
        print(self.timeInIteration)

    def showTemp(self):
        if self.ser.isOpen():
            print(sendAndReceive(self.ser, self.tempAsk))
            return sendAndReceive(self.ser, self.tempAsk)
        else:
            print("Lost connection with chamber")

    def showHumi(self):
        if self.ser.isOpen():
            print(sendAndReceive(self.ser, self.humiAsk))
            return sendAndReceive(self.ser, self.humiAsk)
        else:
            print("Lost connection with chamber")

    def tempData(self):
        if self.ser.isOpen():
            PV, SP, lowVal, maxVal = changeAnsForTable(sendAndReceive(self.ser, self.tempAsk))
            print("TEMP: ", self.timeInIteration.year, self.timeInIteration.month, self.timeInIteration.day,
                  self.timeInIteration.hour, self.timeInIteration.minute, self.timeInIteration.second, PV, SP, lowVal,
                  maxVal)
            return self.timeInIteration.year, self.timeInIteration.month, self.timeInIteration.day, self.timeInIteration.hour, self.timeInIteration.minute, self.timeInIteration.second, PV, SP, lowVal, maxVal
        else:
            print("Lost connection with chamber")

    def humiData(self):
        if self.ser.isOpen():
            PV, SP, lowVal, maxVal = changeAnsForTable(sendAndReceive(self.ser, self.humiAsk))
            print("HUMI: ", self.timeInIteration.year, self.timeInIteration.month, self.timeInIteration.day,
                  self.timeInIteration.hour, self.timeInIteration.minute, self.timeInIteration.second, PV, SP, lowVal,
                  maxVal)
            return self.timeInIteration.year, self.timeInIteration.month, self.timeInIteration.day, self.timeInIteration.hour, self.timeInIteration.minute, self.timeInIteration.second, PV, SP, lowVal, maxVal
        else:
            print("Lost connection with chamber")

    def checkIfItConnected(self):

        # try:
        #     self.ser.isOpen()
        #
        # except serial.SerialException:
        #     print("We have lost connection with chamber, I'm saving data to the files")  # if we later will add data
        #     # to MySQL we need to to add the data to this as well
        #     saveToFile(self.tempTab, " udalo sie tu byc ")
        #     saveToFile(self.tempFile, self.tempTab)  # we don't wont to lose the data
        #     self.tempTab = []
        #     saveToFile(self.humiFile, self.humiTab)  # we don't wont to lose the data
        #     self.humiTab = []
        #     self.counter = 0
        #
        #     print('We\'ve got a problem, i will try to reconnect with the chamber...')
        #     counter = 0
        #     while (not self.ser.isOpen()) and counter < 100:
        #         self.ser = serial.Serial()  # we have to check if this is not a problem
        #         self.ser.port = '/dev/ttyUSB0'  # this could be cause of trouble!!!! if someone changed the port
        #         self.ser.baudrate = 9600
        #         self.ser.polarity = None
        #         self.ser.bytesize = serial.EIGHTBITS
        #         self.ser.stopbits = serial.STOPBITS_ONE
        #         self.ser.timeout = 1
        #         self.ser.write_timeout = 2
        #         self.ser.parity = serial.PARITY_NONE
        #         self.ser.dsrdtr = True
        #
        #         time.sleep(2)  # waiting for changes
        #         counter = counter + 1

        if self.ser.isOpen():
            print("It's connected, we can rock the data!")
        else:
            print("We have lost connection with chamber, I'm saving data to the files")  # if we later will add data
            # to MySQL we need to to add the data to this as well
            saveToFile(self.tempTab, " udalo sie tu byc ")
            saveToFile(self.tempFile, self.tempTab)  # we don't wont to lose the data
            self.tempTab = []
            saveToFile(self.humiFile, self.humiTab)  # we don't wont to lose the data
            self.humiTab = []
            self.counter = 0

            print('We\'ve got a problem, i will try to reconnect with the chamber...')
            counter = 0
            while (not self.ser.isOpen()) and counter < 100:
                self.ser = serial.Serial()  # we have to check if this is not a problem
                self.ser.port = '/dev/ttyUSB0'  # this could be cause of trouble!!!! if someone changed the port
                self.ser.baudrate = 9600
                self.ser.polarity = None
                self.ser.bytesize = serial.EIGHTBITS
                self.ser.stopbits = serial.STOPBITS_ONE
                self.ser.timeout = 1
                self.ser.write_timeout = 2
                self.ser.parity = serial.PARITY_NONE
                self.ser.dsrdtr = True

                time.sleep(2)  # waiting for changes
                counter = counter + 1
