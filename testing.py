import numpy as np
import time
# import MySQLdb
# from pymysql import connect
from chamberClass import Chamber
from functions import *

chamber1 = Chamber()

for i in range(10):
    time.sleep(3)
    chamber1.update()
    np.zeros([50,10])

    chamber1.showHumi()
    print('')
    chamber1.humiData()
    print('')
    print('')

    chamber1.humiData()
    print("")
    print("")











#
# db = connect("localhost", "testuser", "test123", "TESTDB")
#
# cursor = db.cursor()
#
# cursor.execute("SELECT VERSION()")
#
# data = cursor.fetchone()
#
# print("Database version: %s " % data)
#
# db.close()