import sys
def main():
    # Ask the user for input and convert it to a float
    celsius = float(input("Enter temperature in °C: "))

    # Perform the conversion
    fahrenheit = celsius * 9 / 5 + 32

    # Print the result using an f-string
    print(f"{celsius}°C is equal to {fahrenheit}°F")


if __name__ == '__main__':
    sys.exit(main())