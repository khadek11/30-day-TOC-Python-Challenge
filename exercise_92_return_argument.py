import sys

def get_name():
    return "Mercy"

def greet(name: str):
    print(f'Hello, {name}')
def main():
    greet(get_name())
    return 0


if __name__ == '__main__':
    sys.exit(main())