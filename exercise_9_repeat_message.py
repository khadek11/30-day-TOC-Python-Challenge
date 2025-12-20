import sys


def main():
    # ask a user to print a a short message
    message = input("Enter a short message: ")
    #print the message three times, each in a new line
    print((message + "\n")  * 3 )
    return 0


if __name__ == '__main__':
    sys.exit(main())