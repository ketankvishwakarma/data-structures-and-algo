"""
Implement Insertion sort
"""

def insertion_sort(arr):

    for outer_index in range(1,len(arr)):
        current_val = arr[outer_index]
        for sub_index in reversed(range(outer_index)):
            if current_val < arr[sub_index]:
                arr[sub_index+1] = arr[sub_index]
                arr[sub_index] = current_val
    return arr

print(insertion_sort([2,1,9,76,4]))

print(insertion_sort([1,1,1,0,0,2]))

print(insertion_sort([1,2,3,4,5,6]))
print(insertion_sort([0]))
print(insertion_sort([]))