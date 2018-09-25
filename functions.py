import time


def sendAndReceive(serialObject, message):
    serialObject.write(bytearray(message, 'utf-8'))
    time.sleep(0.2)
    ans = serialObject.readline()
    return ans

def sendAndReadFirst(serialObject):
    serialObject.write(b'SRQ?\r\n')
    time.sleep(0.2)
    ans = serialObject.readline()
    return ans


def sendAndReadTemp(serialObject):
    serialObject.write(b'TEMP?\r\n')
    time.sleep(0.2)
    ans = serialObject.readline()
    return ans
