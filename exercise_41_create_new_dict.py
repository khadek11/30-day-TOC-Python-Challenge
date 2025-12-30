import sys


def main():
    #prompt user to enter details
    name = input("What is your name? ")
    birth_year = int(input("What is your birth year? "))
    country = input("What is your country? ")
    #save details in a dictionary
    profile: dict[str, object] = {
        "name": name,
        "birth_year": birth_year,
        "country": country,
    }
    #create a new dict
    new_profile: dict[str, object] = {
        "NAME": name.upper(),
        "age_in_2025": 2025 - birth_year,
        "country": country.lower()
    }
    print(profile)
    print(new_profile)

    return 0


if __name__ == '__main__':
    sys.exit(main())