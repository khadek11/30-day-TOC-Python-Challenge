
def isValid(num):
    while True:
        user = input(num)
        try :
            return int(user)
        except ValueError:
            print("Please enter a valid integer.")

def main():
    val1 = isValid("Enter the First Number: ")
    val2 = isValid("Enter the Second Number: ")

    print(f'The Sum of {val1} and {val2} is: {val1 + val2}')

if __name__ == "__main__":
    main()

## Without checking if the input is an integer
## def main():
## val1 = int(input("Enter the First Number: "))
## val2 = int(input("Enter the Second Number: "))
## print(f'The Sum of {val1} and {val2} is: {val1 + val2}') if __name__ == "__main__": main() )