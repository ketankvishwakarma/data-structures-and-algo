"""
Implement selection sort 
"""

def selection_sort(arr):
    
    for idx in range(len(arr)):
        min_index = idx
        for inner_idx in range(idx,len(arr)):
            if arr[min_index] > arr[inner_idx]:
                min_index = inner_idx
        temp = arr[min_index]
        arr[min_index] = arr[idx]
        arr[idx] = temp
    return arr

print(selection_sort([5,3,4,1,2]))
print(selection_sort([1,2,3,4,5]))
print(selection_sort([4,1,3,5,2]))