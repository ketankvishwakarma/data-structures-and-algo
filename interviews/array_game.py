
"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
https://medium.com/nerd-for-tech/453-minimum-moves-to-equal-array-elements-b79a23684f7f
"""

def countMoves(numbers):
    min_ele = min(numbers)
    total_cost = 0
    for i in range(len(numbers)):
        temp_cost = numbers[i] - min_ele
        total_cost +=temp_cost
    return total_cost

if __name__=="__main__":
    print(countMoves([3,4,6,6,3]))
    print(countMoves([3,2,2,2]))