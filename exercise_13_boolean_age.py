import sys


def main():
    #check if age is a valid
    try:
        #ask the user to input their age
        age = int(input("Enter your age: "))
        #check if age is true or false
        if age >= 18:
            print("True")
        else:
            print("False")
        return 0
    #throw an error if age is not a valid integer
    except ValueError:
        print("Enter a valid age")


if __name__ == '__main__':
    sys.exit(main())