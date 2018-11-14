import DataStruct
from functions import *
import datetime

tempDataTable = []
tempDataTable.append(DataStruct.DataStruct(datetime.datetime(2220,1,1,1,1,1), 10,32,42,12))

tempDataTable.append(DataStruct.DataStruct(datetime.datetime(2220,2,1,1,1,1), 10,32,42,12))

saveTabMySQLTemp('mysql01.saxon.beep.pl',
                'sub_saxon',
                'passwd',
                'test_database',
                 tempDataTable)

