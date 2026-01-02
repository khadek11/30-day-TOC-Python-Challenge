import sys
from itertools import count


def main():
    #ask a user for a word
    word = input("Enter a word: ")
    count = 0
    #print every letter in the word in a new line
    for letter in word:
        print(f"{letter}\n")
        #increase count by one for every letter
        count += 1

    print(f"The total length of the word is {count}")

    return 0


if __name__ == '__main__':
    sys.exit(main())