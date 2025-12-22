import sys


def main():
    #initialize the items list
    items = [20, 30, 40]
    #print this list
    print(f"This is the items list : {items}")
    #create an independent list using slicing
    independent_copy = items[:]
    #print this list
    print(f"This is the independent conpy list {independent_copy}")
    return 0


if __name__ == '__main__':
    sys.exit(main())