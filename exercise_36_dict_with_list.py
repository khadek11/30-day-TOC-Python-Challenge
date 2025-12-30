import sys


def main():
    #prompt user to enter name and three test scores
    user_name = input("What is your name? ")
    first_test_score = int(input("What is your first test score? "))
    second_test_score = int(input("What is your second test score? "))
    third_test_score = int(input("What is your third test score? "))
    scores = [first_test_score, second_test_score, third_test_score]
    #Create a dictionary called student with keys(name and scores)
    student: dict[str, object] = {
        "name": user_name,
        "scores": scores
    }
    #print dict
    print(student)
    #calculate average score
    average_score = float(sum(scores) / len(scores))
    student.setdefault("average", average_score)
    print(student)

    return 0


if __name__ == '__main__':
    sys.exit(main())