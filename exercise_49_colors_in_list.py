import sys


def main():
    #store colors in a list
    colors = ["red", "green", "blue"]
    #prompt user to enter a color
    color = input("Enter a color: ")
    #check if color is in the lost
    if color in colors:
        print("Color available")
    else:
        print("Color not found")
    return 0


if __name__ == '__main__':
    sys.exit(main())