import datetime
import time

while 1:
    period = datetime.datetime.now()

    if period.second %5 ==0:
        print('5 sekund za nami')
        time.sleep(1)