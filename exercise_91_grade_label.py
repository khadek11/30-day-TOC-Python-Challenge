import sys

def grade_label(score):
    return "Pass" if score >= 50 else "Fail"
def main():
    print(grade_label(75))
    print(grade_label(45))

    return 0


if __name__ == '__main__':
    sys.exit(main())