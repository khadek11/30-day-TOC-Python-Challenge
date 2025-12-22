import sys


def main():
    #prompt user to enter five words
    first_word = input("Enter first word: ")
    second_word = input("Enter second word: ")
    third_word = input("Enter third word: ")
    fourth_word = input("Enter fourth word: ")
    fifth_word = input("Enter fifth word: ")
    #store the words in a list
    words = [first_word, second_word, third_word, fourth_word, fifth_word]

    #construct a new list with only words that start with 'a' or 'A'

    a_words = []
    a_words += words[0:1] if words[0].lower().startswith("a") else []
    a_words += (
        words[1:2]
        if words[1].lower().startswith("a")
        else []
    )
    a_words += words[2:3] if words[2].lower().startswith("a") else []
    a_words += words[3:4] if words[3].lower().startswith("a") else []
    a_words += words[4:5] if words[4].lower().startswith("a") else []

    print(a_words)

    return 0


if __name__ == '__main__':
    sys.exit(main())