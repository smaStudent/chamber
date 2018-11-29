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
import time

randomList = ['a', 0, 2]

# for i in range(10):
#     print("iteracja numer: ", i)
#     time.sleep(1)

for entry in randomList:
    try:
        print("The entry is", entry)

        r = 1 / int(entry)

        print("The reciprocal of", entry, "is", r)
        break

    except Exception as e:
        saveProblem(datetime.datetime.now(), e, "Troche lipa, pojawił się problem w testing.py")
        print("Oops!", e, "occured.")
        print("Next entry.")
        print()


def Funkcja(lipa1="dupa"):
    try:
        lipa1 + 312
    except:
        raise


try:
    Funkcja()
except Exception as e:
    print(e)
