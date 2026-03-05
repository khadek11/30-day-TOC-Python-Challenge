import sys

def print_message(message):
    print(f"You entered: {message}")

def main():
    result1 = print_message("Hello, World!")
    result2 = print_message("Welcome to Python programming.")
    result3 = print_message("This is a different input.")
    return 0
    

if __name__ == '__main__':
    sys.exit(main())