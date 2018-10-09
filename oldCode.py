################### OLD CODE ###############################


# def checkIfNotError(self, ans):
#     #tutaj cos trzeba dac

# def sendAndReceive(serialObject, message):
#     serialObject.write(bytearray(message, 'utf-8'))
#     time.sleep(0.2)
#     ans = serialObject.readline()
#     return ans
#
# def sendAndReadFirst(serialObject):
#     serialObject.write(b'SRQ?\r\n')
#     time.sleep(0.2)
#     ans = serialObject.readline()
#     return ans
#
#
# def sendAndReadTemp(serialObject):
#     serialObject.write(b'TEMP?\r\n')
#     time.sleep(0.2)
#     ans = serialObject.readline()
#     return ans


#    def dealWithHeaterOutput(self):
#         global humiHeterOut, heaterOutput, tempNum
#         ansHeterOutput = self.sendAndReceive(self.ser, self.heaterAsk)
#         tempStr = str()
#         whichIter = 0
#         # here check if we didn't get an error
#
#         for c in ansHeterOutput:
#             if c == ',':
#                 whichIter = whichIter + 1
#                 tempStr = str()
#             else:
#                 tempStr = tempStr + c
#
#             tempInt = int(tempStr)
#
#             if whichIter == 0:
#                 tempNum = tempInt
#             if whichIter == 1:
#                 heaterOutput = tempInt
#             if whichIter == 2:
#                 humiHeterOut = tempInt
#
#         self.heaterTable = {'NAME': 'HEATER_OUTPUT', 'TIME': self.timeInIteration, 'NUMBER_OF_HEATERS': tempNum, 'HEATER_OUTPUT': heaterOutput, 'HUMIDIFYING_HEAT_OUT': humiHeterOut}


# self.tempTable = {'NAME': 'TEMP',
#                   'TIME': None,
#                   'PV': None,
#                   'SP': None,
#                   'MIN': None,
#                   'MAX': None}
#
# self.humiTable = {'NAME': 'HUMI',
#                   'TIME': None,
#                   'PV': None,
#                   'SV': None,
#                   'MIN': None,
#                   'MAX': None}
#
# self.heaterTable ={'NAME': 'HEATER_OUTPUT',
#                   'TIME': None,
#                   'NUMBER_OF_HEATERS': None,
#                   'HEATER_OUTPUT': None,
#                   'HUMIDIFYING_HEAT_OUT': None}





############### OLD ONE ##################
#
# def sendAndReadFirst(serialObject):
#     serialObject.write(b'SRQ?\r\n')
#     time.sleep(0.2)
#     ans = serialObject.readline()
#     return ans
#
#
# def sendAndReadTemp(serialObject):
#     serialObject.write(b'TEMP?\r\n')
#     time.sleep(0.2)
#     ans = serialObject.readline()
#     return ans
