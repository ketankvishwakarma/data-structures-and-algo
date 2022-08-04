
def get_binary(N):
    b = []
    while True:
        if N == 0 or N==1:
            b.append(N)
            break
        b.append(N%2)
        N = int(N/2)
    return b
        
def solution(N):
    # write your code in Python 3.6
    binary = get_binary(N)
    print(list(reversed(binary)))
    max_count = 0
    temp_count = 0
    for i in range(len(binary)-1,-1,-1):
        if binary[i]==0:
            temp_count+=1
        if binary[i]==1:
            max_count = max(max_count,temp_count)
            temp_count = 0        
    return max_count

if __name__=="__main__":
    N = 32
    print(solution(N))
    print(solution(15))
    print(solution(1041))

