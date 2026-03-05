import sys


def main(name, age):
    print(f"Hello, {name}! You are {age} years old.")
    age_next_year = age + 1
    return print(f"Next year, you will be {age_next_year} years old.")


if __name__ == '__main__':
    sys.exit(main("Mercy", 25))