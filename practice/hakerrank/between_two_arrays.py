"""
https://www.hackerrank.com/challenges/between-two-sets/problem

"""

"""
Ex1: 
a = 24, b = 60

Pass1: gcd(b%a , a)
       gcd(60%24,24)  ==> 60%24 = 12

Pass2: gcd(12,24)
       gcd(24%12,12)  ==> 24%12 = 0

Pass3: gcd(0,12)
       return 12


Ex2: 
a = 40, b = 64

Pass1: gcd(b%a , a)
       gcd(64%40,40)  ==> 40%64 = 24

Pass2: gcd(24,40)
       gcd(40%24,24)  ==> 40%24 = 16

Pass3: gcd(16,24)
       gcd(24%16,16)  ==> 24%16 = 8

Pass4: gcd(8,16)
       gcd(16%8,8)    ==> 16%8 = 0

Pass5: gcd(0,8)
       return 8



"""
from functools import reduce


def gcd(x,y):
    if x == 0:
        return y
    return gcd(y%x, x)

def lcm(a,b):
    return (a*b) //gcd(a,b)

def lcm_list(l_list: list) -> int:
    return reduce(lcm, l_list)

def gcd_list(g_list: list) -> int:
    return reduce(gcd,g_list)

if __name__=="__main__":
    x = lcm_list([2,3,6])
    y = gcd_list([42,84])
    count = 0
    lowest_factor = x
    count = 0
    while lowest_factor <= y:
        if y%lowest_factor==0:
            count+=1
        lowest_factor = lowest_factor+x
    print(count)