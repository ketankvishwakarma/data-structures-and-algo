def two_numbers_sum_v1(array,target_sum):
    for i,x in enumerate(array):
        for y in range(i+1,len(array)):
            yval = array[y]
            if x+yval==target_sum:
                return [x,yval]
    return []



def two_numbers_sum_v2(array, targetSum):
    hash_map ={}
    for index, value in enumerate(array):
        hash_map[value]=index
    for idx, val in enumerate(array):
        required_val = targetSum - val
        if required_val in hash_map and idx!=hash_map.get(required_val):
            return [val,required_val]
    return []

def two_numbers_sum_v3(array, targetSum):
    array.sort()
    left = 0
    right = len(array) -1
    while(left<right):
        current_sum = array[left] + array[right]
        if current_sum==targetSum:
            return [array[left],array[right]]
        elif current_sum > targetSum:
            right-=1
        elif current_sum < targetSum:
            left+=1
    return []

print(two_numbers_sum_v1([3, 5, -4, 8, 11, 1, -1, 6],10))
print(two_numbers_sum_v2([3, 5, -4, 8, 11, 1, -1, 6],10))
print(two_numbers_sum_v3([3, 5, -4, 8, 11, 1, -1, 6],10))