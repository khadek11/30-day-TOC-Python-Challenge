import sys


def main():
    try:
        #ask user to enter a word
        word = input("Enter a word: ")
        #ask user to enter integer
        num = int(input("Enter an integer: "))
        #repeat word (num) times
        print((word + "\n" ) * num)
        return 0
    except ValueError:
        print("Enter a valid integer")


if __name__ == '__main__':
    sys.exit(main())