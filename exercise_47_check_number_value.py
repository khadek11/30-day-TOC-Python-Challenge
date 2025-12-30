import sys


def main():
    try:
        #prompt user to enter an integer
        num = int(input("Enter a number: "))
        #check if num is less than zero, if True print Negative
        if num < 0:
            print("Negative")
        #check if num is greater than zero, if True print Zero
        elif num == 0:
            print("Zero")
        #if first two are False then print Positive
        else:
            print("Positive")

        return 0
    except ValueError:
        #throw an error uf the input is not an int
        print("Invalid input")


if __name__ == '__main__':
    sys.exit(main())