import sys


def main():
    #set var to 10
    var = int(10)
    print(f"initial Variable is {var}")

    #increase var by 1
    var += 1
    print(f" updated variable using += {var}")

    #set var again to 10
    var = int(10)
    #decrease var by 1
    var -= 1
    print(f" updated variable using -= {var}")

    #set var  t0 10
    var = int(10)
    # multiplied var with an integer
    var *= 2
    print(f" updated variable using *= {var}")

    #set var to 10
    var = int(10)
    #raise var to the power of 3
    var **= 3
    print(f" updated variable using **= {var}")

    return 0



if __name__ == '__main__':
    sys.exit(main())