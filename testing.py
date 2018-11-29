import DataStruct
from functions import *
import datetime
import time



# tempDataTable = []
# tempDataTable.append(DataStruct.DataStruct(datetime.datetime(2220, 1, 1, 1, 1, 1), 10, 32, 42, 12))
#
# tempDataTable.append(DataStruct.DataStruct(datetime.datetime(2220, 2, 1, 1, 1, 1), 10, 32, 42, 12))
#
# # for i in tempDataTable:
# #     print(i.retAsTab())
# #     print(i.dateTime)
# #
# #
# # saveTabMySQLTemp('mysql01.saxon.beep.pl', 'sub_saxon', 'passwd', 'test_database', tempDataTable)
#
# print(tempDataTable[-1])
#


# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:

        print("The entry is", entry)

        r = 1 / int(entry)

        print("The reciprocal of", entry, "is", r)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Next entry.")
        print()

