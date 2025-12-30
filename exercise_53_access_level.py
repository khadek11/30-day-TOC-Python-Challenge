import sys


def main():

    #prompt user to enter username and boolean
    user_name = input("Enter your name: ").strip()
    is_admin_input = input("Are you an admin, True or False? ")
    # Convert string to boolean
    is_admin = is_admin_input.lower() == "true"

    access_level = int(1)
    # Check if user is "admin" or is_admin is True
    if user_name.lower() == "admin" or  is_admin:
        access_level += 4
    else:
        access_level += 1

    print(access_level)
    return 0



if __name__ == '__main__':
    sys.exit(main())