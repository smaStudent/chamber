import numpy as np
import time
# import MySQLdb
from chamberClass import Chamber
from functions import *

chamber1 = Chamber()

for i in range(10):
    time.sleep(1)
    chamber1.update()
    chamber1.showTemp()
    #print('')
    #chamber1.humiData()
    # print('')
    # print('')

    chamber1.tempData()
    print("")
    # print("")
