import time
from ChamberClass import Chamber

import time

time.time(15000)


def main():
    chamber = Chamber()

    time.sleep(15)
    while 1:
        chamber.update()


if __name__ == '__main__':
    main()
