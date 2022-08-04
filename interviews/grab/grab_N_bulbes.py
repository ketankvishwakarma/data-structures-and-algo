

def n_bulbs(n):
    count = 0
    for i in range(len(n)):
        if n[i] <=i+1:
            count+=1
    return count


if __name__=="__main__":
    print(n_bulbs([2,1,3,5,4]))
    print(n_bulbs([2,3,4,1,5]))
    print(n_bulbs([1,3,4,2,5]))