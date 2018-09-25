import time

def sendAndReceive(serialObject, message):
    serialObject.write(bytearray(message, 'utf-8'))
    time.sleep(0.2)
    ans = serialObject.read(8)
    return ans