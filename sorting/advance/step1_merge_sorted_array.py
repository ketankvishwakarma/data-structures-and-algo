def merge_sorted_array(arr1, arr2):
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


print(merge_sorted_array([1,10,50],[2,19,99]))

print(merge_sorted_array([99,101,150],[2,9,10]))

print(merge_sorted_array([99,101,150],[]))
