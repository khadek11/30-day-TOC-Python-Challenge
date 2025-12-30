import sys


def main():
    #prompt user to enter a word
    word = input("Enter a word: ")
    #check if word == python
    if word == "python":
        print("correct word")
    return 0


if __name__ == '__main__':
    sys.exit(main())