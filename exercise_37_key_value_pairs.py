import sys


def main():
    #create the dict
    data = {"a": 1, "b": 2, "c": 3}
    #print the length of the dict
    print(len(data))
    #print result of data.keys()
    print(data.keys())
    #print result of data.values()
    print(data.values())

    return 0


if __name__ == '__main__':
    sys.exit(main())