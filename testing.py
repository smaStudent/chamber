import numpy as np
import time
# import MySQLdb
from chamberClass import Chamber

chamber1 = Chamber()
arrayNp = np.array([0,0,0,0])

for i in range(10):
    time.sleep(1)
    np.append(arrayNp, chamber1.showTemp())

for i in arrayNp:
    print(i)
