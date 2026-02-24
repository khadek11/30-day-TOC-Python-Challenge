import sys


def main():
    #initailize word dict
    words_count = {}
    #open the file
    with open("file.txt") as f:
        #iterate over each line
        for line in f:
            #split line into words
            words = line.lower().split()
            #build a dict counting word occurrences
            for word in words:
                if word in words_count:
                    words_count[word] += 1
                else:
                    words_count[word] = 1
    #print the final dict
    print(words_count)

    return 0


if __name__ == '__main__':
    sys.exit(main())
