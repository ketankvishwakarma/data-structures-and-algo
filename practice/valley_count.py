def countingValleys(steps, path):
    # Write your code here
    valley_count = 0
    previous = 0
    current = 0
    for step in path:
        if step =='D':
            current-=1
        if step == 'U':
            current+=1
        if previous ==0 and current== -1:
            valley_count += 1
        previous = current
    return valley_count

#print(countingValleys(8,['U','D','D','D','U','D','U','U']))
print(countingValleys(8,['D','D','U','U','U','U','D','D']))

print(countingValleys(8,['D','U','D','U','D','U','U','D']))