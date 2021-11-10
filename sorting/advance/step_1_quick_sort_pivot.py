def swap(arr, swap_idx, idx):
    temp = arr[idx]
    arr[idx] = arr[swap_idx]
    arr[swap_idx] = temp

def postion_pivot(arr):
    
    if len(arr) ==1: return 0

    pivot_index = 0
    pivot = arr[pivot_index]
    swap_idx = 0
    
    for i in range(1,len(arr)):
        if pivot > arr[i]:
            swap_idx+=1
            swap(arr,swap_idx,i)
    swap(arr,pivot_index,swap_idx)
    print(arr)
    return swap_idx
        




print(postion_pivot([5,2,1,8,4,3]))