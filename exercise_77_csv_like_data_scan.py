import sys


def main():

    highest_score = 0
    top_scorer = ""
    # used to demonstrate compound assignment
    line_count = 0

    with open("scores.txt") as f:
        next(f)
        for line in f:
            # remove newline
            line = line.lower().strip()
            # split using comma
            parts = line.split(",")

            name = parts[0]
            # numeric conversion
            score = int(parts[1])
            # compound assignment example
            line_count += 1

            if score > highest_score:
                highest_score = score
                top_scorer = name

    print("Top Scorer:", top_scorer)
    print("Highest Score:", highest_score)



    return 0


if __name__ == '__main__':
    sys.exit(main())
