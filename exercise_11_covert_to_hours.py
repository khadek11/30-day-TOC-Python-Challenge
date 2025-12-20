import sys


def main():
    try:
        # ask user for x minutes
        minutes = int(input("Enter your minutes: "))
        #convert X minutes Y to hours
        hours = float(minutes / 60)
        #print both minutes and hours
        print(f"You entered {minutes} minutes which is {hours} hours")
        return 0
    except ValueError:
        print("You can't enter non-numeric minutes")


if __name__ == '__main__':
    sys.exit(main())