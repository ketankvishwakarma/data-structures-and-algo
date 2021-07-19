"""
Question: Write a function called maxSubarraySum which accepts an array of integer and a number callled n.
The function should calculate the maximum sum of n consecutive elements in the array.

Ex:

maxSubarraySum([1,2,5,2,8,1,5],2)     -> 10
maxSubarraySum([1,2,5,2,8,1,5],4)     -> 17
maxSubarraySum([1,2,5,2,6,1,5],1)     -> 6
maxSubarraySum([],4)                  -> None
"""


def compute_sum(array,window_size):
    
    if len(array) ==0:
        return None
    if window_size==0:
        return None
        
    max_sum = 0
    for index, index_itme in enumerate(range(window_size)):
        max_sum = max_sum+array[index]
    
    for index,index_itme in enumerate(range(window_size,len(array))):
        temp_sum = max_sum + array[index] - array[index-window_size]
        if temp_sum>max_sum:
            max_sum=temp_sum
    return max_sum

if __name__ =="__main__":
    array = [1,2,5,2,8,1,5]
    window_size = 2
    print(compute_sum(array=array,window_size=window_size))
    print(compute_sum(array=array,window_size=4))

