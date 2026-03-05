import sys

def is_even(n):
    return True if n % 2 == 0 else False
def main():
    print(is_even(4))
    print(is_even(5))
    print(is_even(0))
    return 0


if __name__ == '__main__':
    sys.exit(main())