import DataStruct
from functions import *
import datetime
import pymysql as mysql


tempDataTable = []
tempDataTable.append(DataStruct.DataStruct(datetime.datetime(2220, 1, 1, 1, 1, 1), 10, 32, 42, 12))

tempDataTable.append(DataStruct.DataStruct(datetime.datetime(2220, 2, 1, 1, 1, 1), 10, 32, 42, 12))

# for i in tempDataTable:
#     print(i.retAsTab())
#     print(i.dateTime)
#
#
#saveTabMySQLTemp('mysql01.saxon.beep.pl', 'sub_saxon', 'passwd', 'test_database', tempDataTable)

print(tempDataTable[-1])

