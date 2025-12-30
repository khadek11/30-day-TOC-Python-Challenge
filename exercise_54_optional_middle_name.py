import sys


def main():
    # Ask for first, middle, and last name
    first_name = input("Enter your first name: ").strip()
    middle_name = input("Enter your middle name (optional): ").strip()
    last_name = input("Enter your last name: ").strip()

    # If middle name is empty, set it to None
    if middle_name == "":
        middle_name = None

    # Print full name
    if middle_name:
        print(f"Full name: {first_name} {middle_name} {last_name}")
    else:
        print(f"Full name: {first_name} {last_name}")

    return 0


if __name__ == '__main__':
    sys.exit(main())