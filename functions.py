import time
import serial
import datetime


def sendAndReceive(serialObject, message):
    serialObject.write(bytearray(message, 'utf-8'))
    time.sleep(0.2)
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


def saveToFile(name, tab):
    file = open(name, "a")
    for i in tab:
        file.write(str(i)[1:-1]+"\n")

    file.close()
