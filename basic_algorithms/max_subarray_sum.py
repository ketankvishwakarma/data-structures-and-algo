"""
Given an array of integers & a number, write a function called maxsubarraysum, which finds the maximum sum
of a subarray with given length of the number passed to the function.

Note: A subarray must consist of consecutive elements from original array.
In the first array [100,200,300] is a subarray but [100,300] is not.

max_subarray_sum([100,200,300,400],2) ==> 700
max_subarray_sum([1,4,2,10,23,3,1,0,20],4) ==> 39
max_subarray_sum([-3,4,0,-2,6,-1],2) ==> 5
max_subarray_sum([3,-2,7,-4,1,-1,4,-2,1],2) ==> 5
max_subarray_sum([2,3],3) ==> NONE
"""
import math

def max_subarray_sum(arr,num):
    
    if len(arr)-1 < num:
        return None
    sub_array_sum = 0
    temp_max_array = []
    for index in range(num):
        sub_array_sum = sub_array_sum+arr[index]
    temp_max_array.append(sub_array_sum)
    for index in range(num,len(arr)):
        sub_array_sum = sub_array_sum + arr[index] - arr[index-num]
        temp_max_array.append(sub_array_sum)
    return (max(temp_max_array))





if __name__=="__main__":
    print(max_subarray_sum([1,2,5,2,8,1,5,4],4))
    print(max_subarray_sum([100,200,300,400],2))
    print(max_subarray_sum([1,4,2,10,23,3,1,0,20],4))
    print(max_subarray_sum([-3,4,0,-2,6,-1],2))
    print(max_subarray_sum([3,-2,7,-4,1,-1,4,-2,1],2))
    print(max_subarray_sum([2,3],3))