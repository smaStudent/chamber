
tempTable = {'NAME': "jen", 'TIME': 76, 'PV': 67, 'SP': 8, 'MIN': 8, 'MAX': 5}

print(str(tempTable))

simpleStr = '2, 56.2, 38.9'
tempStr = str()
for s in simpleStr:
    if s == ',':
        print(tempStr)
        tempStr = str()
    else:
        tempStr = tempStr + s

import datetime

print(datetime.datetime.now())

print(datetime.datetime.now())

date = datetime.datetime.now()

year = date.year
month = date.second

print("\n")
print(year)
print(month)