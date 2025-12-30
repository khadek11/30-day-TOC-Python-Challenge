import sys


def main():
    try:
        #prompt user to enter their age
        age = int(input("Enter your age: "))
        #check if age is at least 18, if True then print adult, if False print Minore
        if age >= 18:
            print("Adult")
        else:
            print("Minor")
        return 0
    except ValueError:
        print("Invalid input")


if __name__ == '__main__':
    sys.exit(main())