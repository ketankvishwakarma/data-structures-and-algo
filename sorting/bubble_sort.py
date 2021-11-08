"""
Implement Bubble Sort
"""

def sort(arr):
    swap = True
    for idx in reversed(range(len(arr))):
        for inner_idx in range(idx):
            swap = False
            print("{} {} ".format(arr[inner_idx],arr[inner_idx+1]))
            if arr[inner_idx]> arr[inner_idx+1]:
                temp = arr[inner_idx]
                arr[inner_idx] = arr[inner_idx+1]
                arr[inner_idx+1] = temp
                swap = True
        if swap == False:
            break
    return arr

print(sort([1,7,3,4,6,]))
