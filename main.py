from ChamberClass import Chamber
import time
def main():


    chamber = Chamber()

    time.sleep(15)
    while 1:
        chamber.update()


if __name__ == '__main__':
    main()