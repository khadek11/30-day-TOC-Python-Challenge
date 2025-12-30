import sys


def main():
    #prompt user to enter two integers a and b
    a = int(input("Enter an integer a: "))
    b = int(input("Enter an integer b: "))
    #check if both integers are greater than zero
    if a > 0 and b > 0:
        print("Both positive")
    # if false print this
    else:
        print("At least one is not positive")
    return 0


if __name__ == '__main__':
    sys.exit(main())