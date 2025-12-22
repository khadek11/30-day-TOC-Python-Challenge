import sys


def main():
    #initialise list
    values = [5, 6, 7, 8]
    # extract the first two elements using slicing
    first_two = values[0:2]
    #print the extracted list
    print(first_two)
    return 0


if __name__ == '__main__':
    sys.exit(main())