import datetime


class DataStruct:
    def __init__(self, dateTime=datetime.datetime(1999, 1, 1, 0, 0, 0, 0), PV=None, SP=None, min=None, max=None):
        # self.dateTime = datetime.datetime.now()
        # self.dateTime.year = dateTime.year
        # self.dateTime.month = dateTime.month
        # self.dateTime.day = dateTime.day
        # self.dateTime.hour = dateTime.hour
        # self.dateTime.minute = dateTime.minute
        # self.dateTime.second = dateTime.second
        # self.dateTime.microsecond = 0
        self.dateTime = datetime.datetime(dateTime.year, dateTime.month, dateTime.day, dateTime.hour,
                                          dateTime.minute, dateTime.second)

        self.PV = PV
        self.SP = SP
        self.minLv = min
        self.maxLv = max

    def __str__(self):
        return self.dateTime.__str__() + str(', ') + str(self.PV) + str(', ') + str(self.SP) + str(', ') + str(
            self.minLv) + str(', ') + str(self.maxLv)

    def saveToFile(self, fileName):
        f = open(fileName, 'a')
        f.write(self.__str__())
        f.close()

    def retAsTab(self):
        return self.dateTime, self.PV, self.SP, self.minLv, self.maxLv

    # self.dateTime.year, self.dateTime.month, self.dateTime.day, self.dateTime.hour, self.dateTime.minute, self.dateTime.second
    def __del__(self):
        self.dateTime = None
        self.PV = None
        self.SP = None
        self.minLv = None
        self.maxLv = None


    def readFromFile(self, fileName):

        with open(fileName) as f:
            for line in f:




