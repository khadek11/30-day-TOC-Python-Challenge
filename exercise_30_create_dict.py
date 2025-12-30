import sys


def main():
    #create a dictionary
    person = {"name": "Alice", "age": 25, "country": "Kenya"}
    #print the dictionary as python represents it
    print(person)
    #print person's name
    print(f"The person's name is {person.get("name")}")
    #print person's age
    print(f"The person's age is {person.get('age')}")
    #change value of age from 25 to 26
    person.update({"age": 26})
    #print updated dictionary
    print(person)
    return 0


if __name__ == '__main__':
    sys.exit(main())