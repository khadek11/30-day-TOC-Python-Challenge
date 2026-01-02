import sys



def main():
    #set the length of the list
    count = 5
    #initialize the list
    numbers = []
    #ask user to enter a number count number of times
    for i in range(count):
        number = int(input(f"Enter a number {i + 1}: "))
        #append the number to the list
        numbers.append(number)
        #check if the number is negative
        if number < 0:
            break
    print(numbers)


    return 0


if __name__ == '__main__':
    sys.exit(main())