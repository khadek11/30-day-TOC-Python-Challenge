import sys


def variable():
    x = 10
variable()
print(x)

if __name__ == '__main__':
    sys.exit()
#NameError: name 'x' is not defined
#Local variables only exist inside the function.
#Once the function finishes executing, x is not accessible outside.
#Therefore, trying to print(x) outside the function causes a NameError