import sys


def main():
    #ask user to input First Word
    first_word= input("Enter first word: ")
    #ask user to input second word
    second_word = input("Enter second Word: ")
    #concatinate both word
    print(f"The words combined are {first_word + " " + second_word}")
    return 0


if __name__ == '__main__':
    sys.exit(main())