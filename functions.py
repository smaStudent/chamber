import time
import serial
import datetime

def sendAndReceive(serialObject, message):
    serialObject.write(bytearray(message, 'utf-8'))
    time.sleep(0.2)
    ans = serialObject.readline()
    ans = ans.decode("utf-8")
    return ans

def saveTableToFile(obj, table):
        for i in table:
            obj.write(str(i))
            obj.write('\n')
        obj.close()

def changeAnsToTable(ans):
    return 'aa'


############### OLD ONE ##################
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
