import datetime
from ChamberClass import Chamber
import time
from functions import saveLog

time.sleep(15)


def main():
    chamber = Chamber()

    while 1:
        chamber.update()

        # we have to make a protection that no matter what we are doing, we'll save our
        # data because we would like to reboot logger every hour

        currentTime = datetime.datetime.now()

        if currentTime.minute > 58:
            chamber.instantPushData()
            saveLog("Hourly reboot, data hopefully is in the database or in the file")


if __name__ == '__main__':
    main()
