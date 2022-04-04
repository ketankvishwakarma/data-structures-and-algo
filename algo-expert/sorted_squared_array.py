def sorted_squared_array(array):
    left_idx = 0
    right_idx = len(array)-1
    out_idx = right_idx
    output = [0] * (len(array))
    while(out_idx>-1):
        r_val = abs(array[right_idx])
        l_val = abs(array[left_idx])
        if r_val > l_val:
            output[out_idx] = r_val ** 2
            right_idx-=1
        elif l_val > r_val or r_val == l_val:
            output[out_idx] = l_val ** 2
            left_idx+=1
        out_idx-=1
    return output


print(sorted_squared_array([-7,-5,-4,3,6,8,9]))
print(sorted_squared_array([-7,-5,3,4,6,8,9]))