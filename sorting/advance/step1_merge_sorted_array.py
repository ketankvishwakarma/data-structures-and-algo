def merge_sorted_array(arr1, arr2):
    sorted_array = []
    first_array_index = 0
    second_array_index = 0
    while first_array_index< len(arr1) and second_array_index< len(arr2):
        if arr1[first_array_index] < arr2[second_array_index]:
            sorted_array.append(arr1[first_array_index])
            first_array_index+=1
        else:
            sorted_array.append(arr2[second_array_index])
            second_array_index+=1
        if first_array_index == len(arr1)-1:
            for i in range(second_array_index,len(arr2)):
                sorted_array.append(arr2[i])
            break
        if second_array_index == len(arr2)-1:
            for i in range(first_array_index,len(arr1)):
                sorted_array.append(arr2[i])
            break


    print(sorted_array)

merge_sorted_array([1,10,50],[2,19,99])
