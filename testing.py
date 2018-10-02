from chamberClass import Chamber
import time

chamber1 = Chamber()

for i in range(100):
    chamber1.update()
    chamber1.showTemp()
    time.sleep(2)
