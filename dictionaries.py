import sys


def main():
    my_dict = dict()
    my_dict.setdefault("Shoes", "Adidas")
    print(my_dict)
    print(my_dict["Shoes"])
    print(
        my_dict.setdefault("Trousers", "Jordan")
    )
    print(my_dict)
    print(my_dict.get("Shoes", "Adidas"))
    print(my_dict.items())
    print(my_dict.popitem())
    print(my_dict.items())
    return 0


if __name__ == '__main__':
    sys.exit(main())