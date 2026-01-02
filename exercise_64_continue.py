import sys


def main():
    #stores number is a list
    values = [10, -4, 35, 467, -5, 7, 8, -9, 10, 0, -6]
    #loop through each number in the list
    for value in values:
        #check if number is positive and print it
        if value <= 0:
            #jump the the next iteration loop
            continue
        print(value)

    return 0


if __name__ == '__main__':
    sys.exit(main())