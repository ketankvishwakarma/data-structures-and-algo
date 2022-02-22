
def max_sub_array_of_size_k(arr,k):
    if len(arr) < k:
        return 0
    first_sum = 0
    array_of_sum = []
    for index in range(0,k):
        first_sum =first_sum + arr[index]
    array_of_sum.append(first_sum)

    for index in range(k,len(arr)):
        working_index =index-k
        item_to_add = arr[index]
        item_to_substract = arr[working_index]
        next_sum = array_of_sum[working_index]+item_to_add-item_to_substract
        array_of_sum.append(next_sum)
    return max(array_of_sum)


def main():
    print("[2,1,5,1,3,2] max sub array for k = 3 is {}".format(max_sub_array_of_size_k([2,1,5,1,3,2],3)))
    print("[2, 3, 4, 1, 5] max sub array for k = 3 is {}".format(max_sub_array_of_size_k([2, 3, 4, 1, 5],3)))

main()
