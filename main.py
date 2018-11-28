import time
from ChamberClass import Chamber

time.time(15000)

def main():
    
    chamber = Chamber()

    
    while 1:
        chamber.update()


if __name__ == '__main__':
    main()
