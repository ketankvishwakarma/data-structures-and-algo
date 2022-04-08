
def merge(arr1, arr2):
    sorted_array = []
    first_array_idx = 0
    secnd_array_idx = 0
    while first_array_idx< len(arr1) and secnd_array_idx < len(arr2):
        if arr1[first_array_idx] < arr2[secnd_array_idx]:
            sorted_array.append(arr1[first_array_idx])
            first_array_idx+=1
        else:
            sorted_array.append(arr2[secnd_array_idx])
            secnd_array_idx+=1
    if first_array_idx < len(arr1):
        for i in range(first_array_idx,len(arr1)):
            sorted_array.append(arr1[i])
    if secnd_array_idx < len(arr2):
        for i in range(secnd_array_idx,len(arr2)):
            sorted_array.append(arr2[i])
    return sorted_array



def merge_sort(arr):
    if len(arr)<=1: return arr
    mid = int(len(arr)/2)
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

    





print(merge_sort([50,1,10,2,19,99]))

#print(merge([1,10,50],[2,19,99]))

#print(merge([99,101,150],[2,9,10]))

#print(merge([99,101,150],[]))
