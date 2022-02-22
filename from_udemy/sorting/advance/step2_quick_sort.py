import random
def swap(arr,swap_idx,idx):
    temp = arr[idx]
    arr[idx] = arr[swap_idx]
    arr[swap_idx] = temp

def pivot(arr,left=0,right=0):
    pivot_idx  = 0
    pivot = arr[pivot_idx]
    swap_idx = 0
    for idx in range(left,right):
        if pivot >= arr[idx]:
            swap_idx +=1
            swap(arr,swap_idx,idx)
    swap(arr,swap_idx,0)
    return swap_idx

def quick_sort(arr,left=0,right=0):
    if(left <= right):
        pivot_idx = pivot(arr,left,right)
        quick_sort(arr,left,pivot_idx-1)
        quick_sort(arr,pivot_idx+1,right)
    return arr




#pivot([0,0,0,0,0,0])
print(quick_sort([1,0,0,0,0,0],0,5))



