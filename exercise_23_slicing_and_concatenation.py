import sys


def main():
    my_list = [10, 20, 30, 40, 50, 60]
    #extracting the middle numbers using slicing alone
    middle_numbers_slicing_alone = my_list[1:5]
    print(middle_numbers_slicing_alone)
    #extractiong the middle numbers using both slicing and concatenation
    middle_numbers_concat_slicing = my_list[1:3] + my_list[3:5]
    print(middle_numbers_concat_slicing)

    return 0


if __name__ == '__main__':
    sys.exit(main())