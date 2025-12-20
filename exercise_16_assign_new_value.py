import sys


def main():
    x = None
    print(f" x is previously {x}")
    #let user assign a  value to x
    x = input("Enter a new value of x: ")
    print(f"The assigned a value to x is {x}")

    return 0


if __name__ == '__main__':
    sys.exit(main())