import sys


def main():
    try:
        #prompt user to enter their details(name, age and city)
        name = input("What is your name? ")
        age = int(input("How old are you? "))
        city = input("Where do you live? ")
        #store details in a list
        profile = {"name": name, "age": age, "city": city}
        #print the list
        print(profile)
        #Add a new key age_next_year whose value is the user’s age plus one
        profile["age_next_year"] = age + 1
        print(profile)
    except ValueError:
        print("Enter a valid integer for age")
    return 0


if __name__ == '__main__':
    sys.exit(main())