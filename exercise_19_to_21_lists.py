import sys


def main():
    #prompt user to enter the first word
    first_word = input("Enter your first word: ")
    #prompt user to enter the second word
    second_word = input("Enter your second word: ")
    #prompt user to enter the third word
    third_word = input("Enter your third word: ")
    #store the words in a list
    list_word =[first_word, second_word, third_word]
    #print the list
    print(list_word)
    #print the first word
    print(f"The first word in your list is {list_word[0]}")
    #print the second word
    print(f"The second word in your list is {list_word[1]}")
    #print the third word
    print(f"The Third word in your list is {list_word[2]}")

    #update the second word with sting "UPDATED"
    list_word[1] = "UPDATED"
    #  print my new list
    print(f"The new updated listed is {list_word}")
    return 0


if __name__ == '__main__':
    sys.exit(main())