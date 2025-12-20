import sys


def main():
    # A variable can change it's type because python uses dynamic typing, Variables point to object
     # such that the data itself(the object) has a type not the variable name.

    #prompt user to enter a number
    num = input("Enter a number: ")
    #reassign that number from a string to a
    num = int(num)
    #pein the value of the variable as an integer type
    print(f"The value of num as an integer is {num} and it's type is {type(num)}")
    #reassign the variable to None Type
    num = None
    #print the value on num as None
    print(f"The value of num is {num} and it's type is {type(num)}")
    return 0


if __name__ == '__main__':
    sys.exit(main())