import sys


def main():
    try:
        number = int(input("Enter a number: "))
        sum = 0
        #condition is true if number is not zero
        while number != 0:
            #summation happens
            sum += number
            number = int(input("Enter a number: "))
            print(f"The total sum of the numbers is {sum}")

        return 0
    except ValueError:
        print("That's not a number.")


if __name__ == '__main__':
    sys.exit(main())