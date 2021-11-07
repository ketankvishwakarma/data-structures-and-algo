"""
Write a function called fib which accepts a number and returns the nth number in the 
Fibonnaci series. Recall that the Fibonacci sequence is the secuence of whole numbers 
1,1,2,3,5,8,... which starts with 1 & 1 and where every number thereafter is equal to the sum of 
the previous two numbers
"""

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(fib(4))
    print(fib(10))
    print(fib(28))
    print(fib(35))