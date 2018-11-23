from ChamberClass import Chamber
def main():
    
    chamber = Chamber()

    chamber.checkCurrentProg()
    
    while 1:
        chamber.update()


if __name__ == '__main__':
    main()