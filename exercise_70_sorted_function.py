import sys


def main():
    # 1. Ask the user for five numbers and store them in a list
    numbers = []
    for i in range(5):
        num = int(input(f"Enter a number {i + 1}: "))
        numbers.append(num)
    print(numbers)
    # 2. Print in ascending order without modifying the original list
    print("\nNumbers in ascending order:")
    for n in sorted(numbers):
        print(n)
    # Verification: Show the original list is still in the input order
    print("\nOriginal list (unchanged):", numbers)
    return 0


if __name__ == '__main__':
    sys.exit(main())