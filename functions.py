# import MySQLdb as mysql
import pymysql as mysql
import sys

import datetime


def sendAndReceive(serialObject, message):
    try:
        serialObject.write(bytearray(message, 'utf-8'))
        #print("SendAdnReceive number 1")
        # time.sleep(0.2) we use flush() instead of time.sleep()
        serialObject.flush()
        #print("SendAdnReceive number 2")
        ans = serialObject.readline()
        #print("SendAdnReceive number 3")
        ans = ans.decode("utf-8")
        #print("SendAdnReceive number 4")
        return ans
    except:
        #print("SendAdnReceive Przypadek się jakiś pierniczy")
        raise


def saveTabMySQLTemp(hostGiven, userGiven, passwdGiven, dbGiven, tab):
    try:
        connection = mysql.connect('mysql01.saxon.beep.pl', 'sub_saxon', 'passwd', 'test_database')
        for obj in tab:
            print("Temp: " + obj.__str__())
            print(obj.retAsTab())
            # year, month, day, hour, minute, second, PV, SP, minLv, maxLv = obj.retAsTab()
            # dateTime, PV, SP, minLv, maxLv = obj.retAsTab()
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO chamberTemp (dateTime, PV, SP, minLevel, maxLevel) VALUES (%s, %s, %s, %s, %s)",
                    (obj.retAsTab()))
                connection.commit()
        connection.close()

    except (mysql.MySQLError, mysql.DataError, mysql.DatabaseError) as e:
        print("Błąd: ", e)
        print("Nie udało się wysłać danuch do MySQL, wpisuję je do pliku...")
        saveTabToFile("tempDataFile.txt", tab)
        print("Dane wpisane do pliku")
        saveProblem(datetime.datetime.now(), comment="Problem pojawił się w funkcji saveTaboMySQLTemp")
        raise


def saveTabMySQLHumi(hostGiven, userGiven, passwdGiven, dbGiven, tab):
    try:
        connection = mysql.connect('mysql01.saxon.beep.pl', 'sub_saxon', 'passwd', 'test_database')
        for obj in tab:
            print("Humi: " + obj.__str__())
            # year, month, day, hour, minute, second, PV, SP, minLv, maxLv = obj.retAsTab()
            # dateTime, PV, SP, minLv, maxLv = obj.retAsTab()
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO chamberHumi (dateTime, PV, SP, minLevel, maxLevel) VALUES (%s, %s, %s, %s, %s)",
                    (obj.retAsTab()))
                connection.commit()
        connection.close()

    except (mysql.MySQLError, mysql.DataError, mysql.DatabaseError) as e:
        print("Błąd: ", e)
        print("Nie udało się wysłać danuch do MySQL, wpisuję je do pliku...")
        saveTabToFile("humiDataFile.txt", tab)
        print("Dane wpisane do pliku")
        saveProblem(datetime.datetime.now(), comment="Problem pojawił się w funkcji saveTaboMySQLHumi")
        raise

    # datetime.datetime(year, month, day, hour, minute, second), PV, SP, minLv, maxLv)

    ########################################
    ######## NOT WORKING OR OLD CODE #######
    ########################################


########################################
#### Functions that are problemless ####
########################################

def retFloatFromString(givStr):
    retFloat = 0.0
    newFirstStr = str()
    newLastStr = str()
    wasThereComma = False

    for c in givStr:
        if c != '.' and not wasThereComma:
            newFirstStr = newFirstStr + c
        elif c != '.' and wasThereComma:
            newLastStr = newLastStr + c
        elif c == '.':
            wasThereComma = True

    if wasThereComma:
        retFloat = float(int(newFirstStr)) + (float(int(newLastStr)) / pow(10, (len(newLastStr))))
    else:
        retFloat = float(int(newFirstStr))
    return retFloat


def changeAnsForTable(ans):
    PV = 0.0
    SP = 0.0
    low = 0.0
    max = 0.0
    tempStr = str()
    iteration = 0

    for c in ans:
        if c != ',':
            tempStr = tempStr + c
        elif c == ',':
            if iteration == 0:
                PV = retFloatFromString(tempStr)
                tempStr = str()
            elif iteration == 1:
                if tempStr != "OFF":
                    SP = retFloatFromString(tempStr)
                tempStr = str()
            elif iteration == 2:
                max = retFloatFromString(tempStr)
                tempStr = str()
            elif iteration == 3:
                low = retFloatFromString(tempStr)
                tempStr = str()
            iteration = iteration + 1

    return PV, SP, low, max


def saveTabToFile(name, tab):
    file = open(name, "a")
    for obj in tab:
        file.write(obj.__str__() + "\n")
    file.close()


def saveObjectToFile(name, obj):
    file = open(name, 'a')
    file.write(obj.__str__())
    file.close()


def saveProblem(timeD, problem=None, comment=None):
    file = open("errorAndExceptionFile.txt", "a")

    file.write(timeD.__str__() + ":\t")

    if problem is None:
        file.write(str(sys.exc_info()[0]))
    else:
        file.write(problem.__str__())
    if comment is not None:
        file.write("\t" + comment)
    file.write("\n")


# import urllib2
# def internet_on():
#     try:
#         urllib2.urlopen('http://216.58.192.142', timeout=1)
#         return True
#     except urllib2.URLError as err:
#         return False
