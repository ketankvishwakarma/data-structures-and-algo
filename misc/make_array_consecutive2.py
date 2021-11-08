def makeArrayConsecutive2(statues):
    statues.sort()
    all_sizes = []
    for x in range(statues[0],statues[(len(statues)-1)]+1):
        all_sizes.append(x)
    missing = 0
    for x in all_sizes:
        if x not in statues:
            missing+=1
    return missing
    

print(makeArrayConsecutive2([6,2,3,8]))