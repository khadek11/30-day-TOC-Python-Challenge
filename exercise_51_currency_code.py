import sys


def main():
    #create a dictionary
    rates: dict[str, float] = {
        "USD": 160.0,
        "EUR": 170.0,
        "GBP": 200.0

    }
    #prompt user to enter a currency code
    currency_code = input("Enter a currency code: ").strip().upper()
    #check if currency_code exists in rates
    if currency_code in rates:
        print(rates[currency_code])
    else:
        print("currency not supported")

    return 0


if __name__ == '__main__':
    sys.exit(main())