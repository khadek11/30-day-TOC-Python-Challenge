import sys


def main():
    #ask user for their name, age and country
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    country = input("Enter your country: ")
    #store the details in a list
    profile = [name, age, country]
    print(profile)
    summary = [profile[0].upper(), profile[1] + 5, profile[2].lower()]
    print(summary)
    return 0


if __name__ == '__main__':
    sys.exit(main())