import sys


def main():
    #ask user to enter word
    word = input("Enter a word: ")
    #check if word is quit
    while word.lower() != "quit":
        print(word)
        word = input("Enter a word: ")

    return 0


if __name__ == '__main__':
    sys.exit(main())