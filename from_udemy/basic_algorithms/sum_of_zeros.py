"""
Question: Given an ordered array finds the first pair of numbers whose sum is exactly ZERO.
"""

# [-4, -3, -2, -1, 1, 2, 3]

def sum_of_zeros(arr):
    left = 0
    right = len(arr)-1

    while(left<right):
        sum_of_extremes = arr[left]+arr[right]
        if sum_of_extremes == 0:
            return [arr[left],arr[right]]
        if sum_of_extremes < 0:
            left=left+1
        else:
            right=right-1
    return None

if __name__ == "__main__":
    print(sum_of_zeros([-4, -3, -2, -1, 0, 5, 7]))
    print(sum_of_zeros([-4, -3, -2, -1, 0, 1, 2]))