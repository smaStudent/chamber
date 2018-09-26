tempTable = {'NAME': "jeden", 'TIME': None, 'PV': None, 'SP': None, 'MIN': None, 'MAX': None}

tempTable[0] = {'NAME': "jen", 'TIME': 76, 'PV': 67, 'SP': 8, 'MIN': 8, 'MAX': 5}

tempTable[1] = {'NAME': "dwa", 'TIME':8, 'PV': 7, 'SP': 7, 'MIN': 6547, 'MAX': 645}



print(str(tempTable))




simpleStr = '2, 56.2, 38.9'
tempStr = str()
for s in simpleStr:
    if s == ',':
        print(tempStr)
        tempStr = str()
    else:
        tempStr = tempStr+s






