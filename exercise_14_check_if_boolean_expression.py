import sys


def main():
    try:
        #ask user to enter the first integer
        first_integer = int(input("Enter the first integer: "))
        #ask user to enter the second integer
        second_integer = int(input("Enter the second integer: "))
        #check if the first integer is greater than the second integer
        if first_integer > second_integer:
            print(True)
        else:
            print(False)
        #check if the first integer is equal to the second integer
        if first_integer == second_integer:
            print(True)
        else:
            print(False)

        #check if the first integer is not equal to second integer
        if first_integer != second_integer:
            print(True)
        else :
            print(False)

        return 0
    #throw error if the numbers are nit valid integers
    except ValueError:
        print("Please enter a valid integer")


if __name__ == '__main__':
    sys.exit(main())