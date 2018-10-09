import numpy as np
import time
# import MySQLdb
# from pymysql import connect
from chamberClass import Chamber
from functions import *

# chamber1 = Chamber()

w = []
T = []

w.append([2018, 10, 9, 8, 7, 22, 100.0, 0.0, 0.0, 100.0])
T.append([2018, 10, 9, 8, 7, 22, 26.6, 130.0, 0.0, 190.0])
w.append([2018, 10, 9, 8, 7, 26, 100.0, 0.0, 0.0, 100.0])
T.append([2018, 10, 9, 8, 7, 26, 26.6, 130.0, 0.0, 190.0])
w.append([2018, 10, 9, 8, 7, 31, 100.0, 0.0, 0.0, 100.0])
T.append([2018, 10, 9, 8, 7, 31, 26.6, 130.0, 0.0, 190.0])
w.append([2018, 10, 9, 8, 7, 35, 100.0, 0.0, 0.0, 100.0])
T.append([2018, 10, 9, 8, 7, 35, 26.6, 130.0, 0.0, 190.0])
w.append([2018, 10, 9, 8, 7, 39, 100.0, 0.0, 0.0, 100.0])
T.append([2018, 10, 9, 8, 7, 39, 26.6, 130.0, 0.0, 190.0])
w.append([2018, 10, 9, 8, 7, 44, 100.0, 0.0, 0.0, 100.0])
T.append([2018, 10, 9, 8, 7, 44, 26.6, 130.0, 0.0, 190.0])
w.append([2018, 10, 9, 8, 7, 48, 100.0, 0.0, 0.0, 100.0])
T.append([2018, 10, 9, 8, 7, 48, 26.6, 130.0, 0.0, 190.0])
w.append([2018, 10, 9, 8, 7, 52, 100.0, 0.0, 0.0, 100.0])
T.append([2018, 10, 9, 8, 7, 52, 26.6, 130.0, 0.0, 190.0])
w.append([2018, 10, 9, 8, 7, 57, 100.0, 0.0, 0.0, 100.0])
T.append([2018, 10, 9, 8, 7, 57, 26.6, 130.0, 0.0, 190.0])
w.append([2018, 10, 9, 8, 8, 1, 100.0, 0.0, 0.0, 100.0])
T.append([2018, 10, 9, 8, 8, 1, 26.6, 130.0, 0.0, 190.0])

tempFile = 'tempData.txt'
humiFile = 'humiData.txt'


for i in T:
    print(i)

T = []
print("2")
for i in T:
    print(i)
#
#
# for i in range(10):
#     time.sleep(3)
#     chamber1.update()
#     np.zeros([50,10])
#
#     # chamber1.humiData()
# print('')
# print('')
#
# chamber1.humiData()
# print("")
# print("")
#


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
