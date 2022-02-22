import math
def smallest_subarray_with_greater_sum(arr,X):
    if len(arr)<2:
        return 0
    if X==0:
        return 0
    start=0
    min_lenght = math.inf
    window_sum = 0
    
    for end_index in range(0,len(arr)):
        window_sum +=arr[end_index]

        while window_sum>=X:
            value_to_substract = arr[start]
            window_sum -= value_to_substract
            min_lenght = min(min_lenght,end_index-start+1)
            start+=1

    return min_lenght



def main():
    print("[2, 1, 5, 1, 3 ,2] for X = 7 is {}".format(smallest_subarray_with_greater_sum([2,1,5,1,3,2],7)))
    print("[2, 1, 5, 2, 3, 2] for X = 7 is {}".format(smallest_subarray_with_greater_sum([2, 1, 5, 2, 3, 2],7)))
    print("[2, 1, 5, 9, 2, 8] for X = 7 is {}".format(smallest_subarray_with_greater_sum([2, 1, 5, 9, 2, 8],7)))
    print("[3, 4, 5, 1, 1, 6] for X = 8 is {}".format(smallest_subarray_with_greater_sum([3, 4, 5, 1, 1, 6],8)))

main()