import sys

def isValid(num):
    while True:
        user = input(num)
        try:
            return int(user)
        except ValueError:
            print("Please enter a valid integer.")


def main():
    integer = isValid("Enter an integer: ")
    square_integer = integer ** 2
    cube_integer = integer ** 3
    print(f'The square of integer is {square_integer} and the cube of integer is {cube_integer}')


if __name__ == '__main__':
    sys.exit(main())