import sys


def main():
    #save the numbers in a list
    numbers = [10, 20, 30, 40]
    total_sum = 0
    #print the values in the list in a new line for each
    for number in numbers:
        print(f"{number}\n")
        #add up the numbers in the sum
        total_sum += number
    print(f"The total sum of the numbers is {total_sum}")
    return 0


if __name__ == '__main__':
    sys.exit(main())