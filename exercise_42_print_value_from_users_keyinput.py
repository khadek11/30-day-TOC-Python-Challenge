import sys


def main():
    #create new dicy
    grades: dict[str, int] = {
        "A": 80,
        "B": 70,
        "C": 60,
        "D": 50
    }
    #prompt the user to enter a grad letter
    grade_letter = input("Enter a grade letter from A, B, C, or D: ").strip().upper()

    #print value that has that grade_letter or key
    if grade_letter in grades:
        print(f"Minimum score for {grade_letter} is {grades[grade_letter]}")
    else:
        print("Invalid grade")
    return 0


if __name__ == '__main__':
    sys.exit(main())