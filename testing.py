import numpy as np
import time
# import MySQLdb
from chamberClass import Chamber

chamber1 = Chamber()
arrayNp = np.array()

for i in range(100):
    time.sleep(1)
    np.append(arrayNp, chamber1.showTemp())


for i in range(100):
    print(arrayNp[i])