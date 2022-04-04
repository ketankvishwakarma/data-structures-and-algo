def jump_clouds(array):
    count=0
    idx =0
    while(idx<len(array)-1):
        idx = idx+2
        if idx > len(array)-1 and array[idx-1]==0:
            count+=1
            return count
        if array[idx]==0:
            count+=1
        if array[idx]==1:
            idx -=1
            count+=1
    print(count)




print(jump_clouds([0,1,0,0,0,1,0]))

print(jump_clouds([0,0,1,0,0,1,0]))

print(jump_clouds([0,0,0,1,0,0]))