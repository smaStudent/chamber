import pymysql as mysql
import time
import datetime
import pymysql.cursors

connection = mysql.connect(host='mysql01.saxon.beep.pl',
                           user='sub_saxon',
                           passwd='passwd',
                           db='test_database')

try:
    with connection.cursor() as cursor:
        # Create a new record

        cursor.execute("INSERT INTO testing (dateTime, temp, humi) VALUES (%s, %f, %f)",
                       (str(datetime.datetime.now()), str(150.0), str(300.0)))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT `time`, `temp` FROM 'chamber'"
    #     cursor.execute(sql, ('',))
    #     result = cursor.fetchone()
    #     print(result)
finally:
    connection.close()

#
# def insertIntoMySQL(year, month, day, hour, minutes, seconds, temp_PV, temp_SV, temp_min, temp_max, humi_PV, humi_SV, humi_min, humi_max):
#     try:
#         with connection.cursor() as cursor:
#
#             cursor.execute("INSERT INTO chamber (year, month, day, hour, minutes, second, temp_PV, temp_SP, temp_min_LV, temp_max_LV, humi_PV, humi_SP, humi_min_LV, humi_max_LV) VALUES (%)",
#                        (str(time.time()), str(150), str(300)))
#
#

##################################################################################################
##################################################################################################
##################################################################################################
# import numpy as np
# import time
# # import MySQLdb
# # from pymysql import connect
# from chamberClass import Chamber
# from functions import *
#
# # chamber1 = Chamber()
#
# w = []
# T = []
#
# w.append([2018, 10, 9, 8, 7, 22, 100.0, 0.0, 0.0, 100.0])
# T.append([2018, 10, 9, 8, 7, 22, 26.6, 130.0, 0.0, 190.0])
# w.append([2018, 10, 9, 8, 7, 26, 100.0, 0.0, 0.0, 100.0])
# T.append([2018, 10, 9, 8, 7, 26, 26.6, 130.0, 0.0, 190.0])
# w.append([2018, 10, 9, 8, 7, 31, 100.0, 0.0, 0.0, 100.0])
# T.append([2018, 10, 9, 8, 7, 31, 26.6, 130.0, 0.0, 190.0])
# w.append([2018, 10, 9, 8, 7, 35, 100.0, 0.0, 0.0, 100.0])
# T.append([2018, 10, 9, 8, 7, 35, 26.6, 130.0, 0.0, 190.0])
# w.append([2018, 10, 9, 8, 7, 39, 100.0, 0.0, 0.0, 100.0])
# T.append([2018, 10, 9, 8, 7, 39, 26.6, 130.0, 0.0, 190.0])
# w.append([2018, 10, 9, 8, 7, 44, 100.0, 0.0, 0.0, 100.0])
# T.append([2018, 10, 9, 8, 7, 44, 26.6, 130.0, 0.0, 190.0])
# w.append([2018, 10, 9, 8, 7, 48, 100.0, 0.0, 0.0, 100.0])
# T.append([2018, 10, 9, 8, 7, 48, 26.6, 130.0, 0.0, 190.0])
# w.append([2018, 10, 9, 8, 7, 52, 100.0, 0.0, 0.0, 100.0])
# T.append([2018, 10, 9, 8, 7, 52, 26.6, 130.0, 0.0, 190.0])
# w.append([2018, 10, 9, 8, 7, 57, 100.0, 0.0, 0.0, 100.0])
# T.append([2018, 10, 9, 8, 7, 57, 26.6, 130.0, 0.0, 190.0])
# w.append([2018, 10, 9, 8, 8, 1, 100.0, 0.0, 0.0, 100.0])
# T.append([2018, 10, 9, 8, 8, 1, 26.6, 130.0, 0.0, 190.0])
#
# tempFile = 'tempData.txt'
# humiFile = 'humiData.txt'
#
#
# for i in T:
#     print(i)
#
# T = []
# print("2")
# for i in T:
#     print(i)
# #
# #
# # for i in range(10):
# #     time.sleep(3)
# #     chamber1.update()
# #     np.zeros([50,10])
# #
# #     # chamber1.humiData()
# # print('')
# # print('')
# #
# # chamber1.humiData()
# # print("")
# # print("")
# #
#
#
# #
# # db = connect("localhost", "testuser", "test123", "TESTDB")
# #
# # cursor = db.cursor()
# #
# # cursor.execute("SELECT VERSION()")
# #
# # data = cursor.fetchone()
# #
# # print("Database version: %s " % data)
# #
# # db.close()
