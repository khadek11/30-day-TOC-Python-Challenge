import sys


#define function
def greet(name):
    print(f"Hello, {name}")
user_name = input("What is your name? ")
greet(user_name)

#call the function
if __name__ == '__main__':
    sys.exit()
