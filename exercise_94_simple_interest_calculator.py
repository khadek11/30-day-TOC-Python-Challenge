import sys

def interest(principal, rate, time):
    return (principal * rate * time) / 100


def total_amount(principal, interest):
    return principal + interest

def main():
    principal = 1000
    rate = 5
    time = 2
    interest_amount = interest(principal, rate, time)
    total = total_amount(principal, interest_amount)
    print(f"Simple Interest: {interest_amount}")
    print(f"Total Amount: {total}")
    return 0


if __name__ == '__main__':
    sys.exit(main())