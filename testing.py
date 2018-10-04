import numpy as np
import time
 #import MySQLdb
from chamberClass import Chamber
from functions import *

chamber1 = Chamber()
arrayNp = np.array(chamber1.showTemp())

for i in range(10):
    time.sleep(1)
    print("odp bezposrednia", chamber1.showTemp())
    print(changeAnsForTable(chamber1.showTemp()))

for i in arrayNp:
    print(i)











