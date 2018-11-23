# import MySQLdb as mysql
import pymysql as mysql
import datetime


def sendAndReceive(serialObject, message):
    if serialObject.isOpen():
        serialObject.write(bytearray(message, 'utf-8'))
        # time.sleep(0.2) we use flush() instead of time.sleep()
        serialObject.flush()
        ans = serialObject.readline()
        ans = ans.decode("utf-8")
        return ans


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
    obj.__str__()
    file.close()


def saveTabMySQLTemp(hostGiven, userGiven, passwdGiven, dbGiven, tab):
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


def saveTabMySQLHumi(hostGiven, userGiven, passwdGiven, dbGiven, tab):
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

    # datetime.datetime(year, month, day, hour, minute, second), PV, SP, minLv, maxLv)






