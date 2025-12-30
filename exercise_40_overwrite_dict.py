import sys


def main():
    #create new dict
    settings: dict[str,int] = {"volume": 5}
    #overwrite volume to 10
    settings["volume"] = 10
    print(settings)
    return 0


if __name__ == '__main__':
    sys.exit(main())