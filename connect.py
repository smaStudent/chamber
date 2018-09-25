import serial
import time
from functions import sendAndReceive

# import io
ser = serial.Serial()
ser.port = "COM3"
# ser.port = '/dev/ttyS4'
ser.baudrate = 9600
ser.polarity = None
ser.bytesize = serial.EIGHTBITS
ser.stopbits = serial.STOPBITS_ONE
ser.timeout = 1
ser.write_timeout = 2
ser.parity = serial.PARITY_NONE
ser.dsrdtr = True

# to jest chwilowe do sprawdzenia sio
# ser.open()
# print(ser.isOpen())
# sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser),newline = None)
# sio.write(unicode("SRQ?"))
# time.sleep(1)
# sio.flush()
# x = sio.readline()
# print(len(x))
# print(x)

# sio.write(unicode("TEMP?"))
# sio.flush()
# time.sleep(1)
# x = sio.readline()
# print(len(x))
# print(x)


firstString = 'SRQ?'
tempAsk = 'TEMP?'
humiAsk = 'HUMI?'
finishString = '\r\n'  # \r
ser.open()
print(ser.isOpen())
print(ser.name)

if ser.isOpen():
    ans = sendAndReceive(ser, finishString+finishString)
    print('Ans for \'SRQ?\'')
    print(str(ans) + 'Length: ' + str(len(ans)))

for i in range(10):
    ans = sendAndReceive(ser, tempAsk+finishString)
    print(str(i) + '. ans for \'TEMP?\'' + '  Lenght: ' + str(len(ans)))
    print(ans)

    time.sleep(1)
ser.close()

if (not ser.isOpen):
    print('port zamknieto z sukcesem')
else:
    print('nie udalo sie zamknac portu')
