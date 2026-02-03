import sys


def main():
    #store scores in a list
    test_scores = [10, 75, 23, 56, 56, 17, 59, 34]
    #get average
    average_score = sum(test_scores) / len(test_scores)
    #find the scores greater than fifty
    greater_than_fifty = [score for score in test_scores if score >= 50]
    #print the average score of the whole test_score
    print("The average score of the whole test scores is:", average_score)
    #print the list of the scores greater than fifty
    print("The greater score is:", greater_than_fifty)
    #find the average score of scores greater than fifty
    average_greater_than_fifty = sum(greater_than_fifty) / len(greater_than_fifty)
    print("The average score of values greater than Fifty is:", average_greater_than_fifty)

    return 0


if __name__ == '__main__':
    sys.exit(main())