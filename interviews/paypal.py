"""
Title: Parade in Hakerland

Input : 001011

Whenever the is a 01 replace with with 10 and repete it till there is not combination exist.

t0 = 00 10 11
t1 = 01 01 01  --Pass 1
t2 = 11 01 01  --Pass 2
t3 = 111 010   --Pass 3
t4 = 1111 00   --Pass 4

Output = 4
"""


def parade(color):
    
    list1=[]
    list1[:0]=color
    size = len(list1)
    for x in range(size-1):
        temp_x = x
        while(temp_x<size-1):
            if list1[temp_x] == '0' and list1[temp_x+1] == '1':
                list1[temp_x]='1'
                list1[temp_x+1]='0'
            temp_x =temp_x+1
    count =0
    for x in list1:
        if x == '1':
            count = count +1
    return count



if __name__=="__main__":
    print(parade("0101"));
