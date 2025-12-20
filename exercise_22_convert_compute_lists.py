import sys


def main():
    first_num = input("Enter first number: ")
    second_num = input("Enter second number: ")
    third_num = input("Enter third number: ")

    num_list = [first_num, second_num, third_num]
    #print previous number list before conversion
    print(f"The previous list is {num_list}")
    num_list[0] = int(first_num)
    num_list[1] = int(second_num)
    num_list[2] = int(third_num)

    #print the new list after conversion
    print(f"The new list is {num_list}")
    # compute total
    Total = num_list[0] + num_list[1] + num_list[2]
    print(f"The total is {Total}")
    return 0




if __name__ == '__main__':
    sys.exit(main())