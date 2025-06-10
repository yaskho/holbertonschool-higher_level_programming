#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    numbers = [int(num)for num in argv[1:]]
    print(sum(numbers))
