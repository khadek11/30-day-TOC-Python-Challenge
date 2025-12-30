import sys


def main():
    #create new dict
    stats = {
        "count": 10,
        "average": 4.5,
        "valid": True

    }
    #print each value individually using keu access
    print(stats["count"])
    print(stats["average"])
    print(stats["valid"])

    #update count by increasing it to 5 using compound assignment
    stats["count"] += 5

    #updating valid tp false
    stats.update({"valid" : False})
    print(stats)
    return 0


if __name__ == '__main__':
    sys.exit(main())