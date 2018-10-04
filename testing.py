import numpy as np
import time
 #import MySQLdb
from chamberClass import Chamber
from functions import *

chamber1 = Chamber()

for i in range(10):
    time.sleep(1)
    chamber1.showHumi()
