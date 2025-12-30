import sys


def main():
    #prompt user to enter an input
    value = input("Enter an input: ")
    #check if value is empty
    if not value:
        print("No input provided")
    #check if value has an int type
    elif value.isdigit():
        print("Numeric input")
    #else if both are false, print text input
    else:
        print("Text input")
    return 0


if __name__ == '__main__':
    sys.exit(main())