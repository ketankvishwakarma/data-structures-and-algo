"""
https://www.hackerrank.com/challenges/kangaroo/problem
"""

def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 > v1:
        return "NO"
    if v1==v2:
        return "NO"
    if (x2-x1) % (v2-v1)==0:
        return "YES"
    else:
        return "NO"

if __name__=="__main__":
    #print(kangaroo(0,2,5,3))
    print(kangaroo(43,2,70,2))