def left_rotation(a,d):
    
    new_array = [0] * len(a) 
    for i in range(len(a)):
        new_idx = (i+d) % len(a)
        new_array[i] = a[new_idx]
    print(new_array)
left_rotation([1,2,3,4,5],2)
print("-------------------")
left_rotation([1,2,3,4,5],4)