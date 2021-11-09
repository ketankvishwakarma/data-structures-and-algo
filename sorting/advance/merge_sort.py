
def merge(arr1, arr2):
    sorted_array = []
    first_array_index = 0
    second_array_index = 0
    while first_array_index < len(arr1) and second_array_index < len(arr2):
        if arr1[first_array_index] < arr2[second_array_index]:
            sorted_array.append(arr1[first_array_index])
            first_array_index+=1
        else:
            sorted_array.append(arr2[second_array_index])
            second_array_index+=1  

    if first_array_index == len(arr1):
        for i in range(second_array_index,len(arr2)):
            sorted_array.append(arr2[i])

    if second_array_index == len(arr2):
        for i in range(first_array_index,len(arr1)):
            sorted_array.append(arr1[i])

    return sorted_array



def megr_sort(arr):
    if len(arr) <= 1: return arr
    mid = int(len(arr)/2)
    left = megr_sort(arr[0:mid])
    right = megr_sort(arr[mid:])
    return merge(left,right)


print(megr_sort([]))
print(megr_sort([1,1]))
print(megr_sort([1,2,3,4,5,6,7,8,9]))
print(megr_sort([9,8,7,6,5,5,3,2,1]))
