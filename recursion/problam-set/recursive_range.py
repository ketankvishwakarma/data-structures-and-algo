"""
Write a function which accepts a number and adds up all the numbers 
from 0 to the number passed to the function.
"""

def recursive_range(num):
    if num == 1:
        return 1
    return num + recursive_range(num -1)


if __name__ == "__main__":
    print(recursive_range(3))
    print(recursive_range(6))
    print(recursive_range(10))