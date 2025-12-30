import sys


def main():
    #prompt user to enter an  integer
    num = int(input("Enter a number: "))
    #check if num is greater than 10
    if num > 10:
        print("Larger number than 10")
    return 0


if __name__ == '__main__':
    sys.exit(main())