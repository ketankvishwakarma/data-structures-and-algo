def repeated_string(s, n):
    # Write your code here
    count=0
    for x in s:
        if x == "a":
            count+=1
    div = int(n/len(s))
    rem = int(n%(len(s)))
    
    rem_count = 0
    for x in range(rem):
        if s[x]=="a":
            rem_count+=1
    return int((count * div) + rem_count)

print(repeated_string("aba",10))

print(repeated_string("a",1000000000000))