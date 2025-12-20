import sys


def main():
    #ask a user for an integer
    try:
        num = int(input("Enter an integer: "))
        #print original integer
        print(f"Original integer is: {num}")
        # convert to float
        print(f"converted integer to float {float(num)}")
        return 0
    # throw error when num is not an integer
    except ValueError:
        print("That's not an integer")


if __name__ == '__main__':
    sys.exit(main())