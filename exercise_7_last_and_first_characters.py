import sys


def main():
    #ask user to input integer
    word = input("Enter any word: ")
    #print the first character and last character
    print(f"first character of the word is: {word[0]} and the last character of the word is {word[-1]}")
    return 0


if __name__ == '__main__':
    sys.exit(main())