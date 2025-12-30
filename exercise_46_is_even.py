import sys


def main():
    try:
        #prompt user to enter a number
        num = int(input("Enter a number: "))
        #check if num is even, if True print Even number if False print Odd Number
        is_even = num % 2 == 0
        if is_even:
            print("Even Number")
        else:
            print("Odd Number")

    except ValueError:
        #throw error if num is not an integer
        print("Enter a valid integer")



if __name__ == '__main__':
    sys.exit(main())