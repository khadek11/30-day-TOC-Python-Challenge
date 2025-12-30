import sys


def main():
    #prompt user to enter four numbers
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    third_number = int(input("Enter third number: "))
    fourth_number = int(input("Enter fourth number: "))
    #store the numbers in a list num
    nums = [first_number, second_number, third_number, fourth_number]
    print(f"The initial list is {nums}")
    #replace the first number with its square
    nums[0] = first_number ** 2
    #replace the last numder with its cube
    nums[3] = fourth_number ** 3
    print(f"The modified list is {nums}")
    #compute the sum of the elements in the list
    sum = nums[0] + nums[1] + nums[2] + nums[3]
    print(f"The sum of elements in the list is {sum}")
    return 0


if __name__ == '__main__':
    sys.exit(main())