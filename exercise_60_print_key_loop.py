import sys


def main():
    #store data in a dict
    person = {"name": "Alice", "age": 30, "city": "Nairobi"}
    #print the key in the dictionary
    for key in person:
        #print key in dict
        print(key)
        #print the values
        print(person[key])
        #a  36
        print(f"{key} -> {person[key]}")
    return 0


if __name__ == '__main__':
    sys.exit(main())