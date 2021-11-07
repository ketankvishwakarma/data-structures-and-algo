"""
Write a function called min_subarray_len which accepts two parameters an positive integer and a positive number.
This function should return a minimal lenght of a contiguous subarray of which the sum is greater then or equal to the integer passes to the function.
If there isn't one return 0 instead.
"""

import math
def min_subarray_len(arr, num):
    if len(arr) < 1:
        return 0
    start = 0
    end = 0
    min_len = []
    total = 0
    while start < len(arr):
        
        if total < num and end < len(arr):
            total = total+arr[end]
            end +=1
        elif total >= num:
            min_len.append(end - start)
            total = total - arr[start]
            start +=1
        else:
            break
       
    print(min_len)

    return min(min_len)



if __name__ == "__main__":
    print(min_subarray_len([1,2,3,1,3,4,3],7))
    print(min_subarray_len([2,1,6,5,4],9))
    print(min_subarray_len([3,1,7,11,2,9,8,21,62,33,19],52))