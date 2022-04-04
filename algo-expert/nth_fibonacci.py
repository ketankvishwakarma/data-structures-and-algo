def nth_fibonacci(n):
    if n==1 :
        return 0 
    if n == 2: 
        return 1 
    return nth_fibonacci(n-1) + nth_fibonacci(n-2)


def nth_fib_memo(n,memo):
    if n in memo:
        return memo[n]
    else:
        memo[n] = nth_fib_memo(n-1, memo) + nth_fib_memo(n-2,memo)
        return memo[n]


print(nth_fib_memo(5,{1:0,2:1}))



print(nth_fibonacci(5))
print(nth_fibonacci(2))
print(nth_fibonacci(10))
print(nth_fibonacci(11))