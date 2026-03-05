import sys

def greet(name: str, greeting = 'Hello'):
    print(f'{greeting}, {name}')

def main():
    greet("Mercy")
    return 0


if __name__ == '__main__':
    sys.exit(main())