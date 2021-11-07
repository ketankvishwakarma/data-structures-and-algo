"""
Write a recursive function called some_recursive which accepts an array and a callback.
The function returns true if a single value in the array returns true when passed to callback, otherwise false.
"""

def is_odd(value):
    print("checking {} is odd".format(value))
    return value %2 != 0

def is_greaterthen10(value):
    print("checking {} is greater than 10".format(value))
    return value >= 10

def some_recursive(numbers,callback):
    if len(numbers) == 0:
        return False
    if callback(numbers[0])==True:
        return True
    return some_recursive(numbers[1::],callback)

if __name__ == "__main__":
    print(some_recursive([1,2,3,4],is_odd))
    print(some_recursive([2,4,6,8],is_odd))
    print(some_recursive([2,4,6,8],is_odd))
    print(some_recursive([2,4,6,18],is_greaterthen10))