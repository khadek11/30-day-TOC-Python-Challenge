import sys


def main():
    try:
        val1 = int(input("Enter the first number: "))
        val2 = int(input("Enter the second number: "))

        print(f"Quotient : {val1 / val2}")
        print(f"Integer division is: {val1 // val2}")
        print(f"The Remainder of the quotient is {val1 % val2}")
    except ZeroDivisionError:
        print("You can't divide by zero")
    except ValueError:
        print("Please Enter a Valid Integer")
    return 0


if __name__ == '__main__':
    sys.exit(main())
