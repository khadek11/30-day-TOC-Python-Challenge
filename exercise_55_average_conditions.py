import sys

from nltk.metrics import scores


def main():
    try:
        #ask user to enter name and three test scores
        user_name = input("Enter your name: ")
        first_score = int(input("Enter your first score: "))
        second_score = int(input("Enter your second score: "))
        third_score = int(input("Enter your third score: "))
        #store the data in a dictionary
        student: dict[str] = {
            "name": user_name,
            "scores": [first_score, second_score, third_score]

        }
        #calculate the average score
        average_score = float(sum(student["scores"]) / len(student["scores"]))
        #add average score to the dictionary
        student["average_score"] = average_score
        #True if avarage score is above 70
        if student["average_score"] >= 70:
            status = "Pass"
        #True if average score is between 50 and 70
        elif student["average_score"] >= 50 and student["average_score"] < 70:
            status = "Supplementary"
        #if both are false , status is set to fail
        else:
            status = "fail"
        #add statud to the dictionary
        student["status"] = status
        #print the dictionary
        print(student)

        return 0
    except ValueError:
        print("Enter a Valid number")

if __name__ == '__main__':
    sys.exit(main())