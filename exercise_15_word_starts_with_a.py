import sys

from sqlalchemy.sql.operators import truediv


def main():
    #ask user to enter a word
    word = input("Enter a word: ")
    #check if word starts with letter A or a
    if word.lower().startswith("a"):
        print(True)
        print(f"{word} starts with a letter 'a' or 'A")
    else:
        print(False)
        print(f"{word} does not start with a letter 'a' or 'A")

    return 0


if __name__ == '__main__':
    sys.exit(main())