import sys


def main():
    #ask user to enter three words
    #user stripe to remove spaces so that " " doesn't count as a word
    first_word = input("Enter the first word: ").strip()
    second_word = input("Enter the second word: ").strip()
    third_word = input("Enter the third word: ").strip()
    #store the words im a list
    words = [first_word, second_word, third_word]
    #check if at least one string element is non-empty
    if any(words):
        print("list has Items")
    else:
        print("Empty list")
    return 0


if __name__ == '__main__':
    sys.exit(main())