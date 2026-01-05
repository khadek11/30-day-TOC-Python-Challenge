import sys


def main():
    #set n  to 5
    n = 5
    #run only when n is greater than zero
    while n > 0:
        print(n)
        n -= 1

    return 0
    #What happens if the suite does not include a statement that modifies the variable in the assignment expression? Try it!
    #The condition stays True, causing an endless output leading the program to hang

if __name__ == '__main__':
    sys.exit(main())