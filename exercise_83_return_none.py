import sys

def print_message():
    print("This function does not return anything.")
def main():
    result = print_message()
    print(result)  # This will print 'None' since print_message does not return anything.
    
    return 0


if __name__ == '__main__':
    sys.exit(main())