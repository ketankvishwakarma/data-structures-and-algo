"""                                  
"""
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)


if __name__ =="__main__":
    print(factorial(4))