"""
Write a function called binary_search which accepts a sorted array and a value & returns the index
at which the value exists otherwise return -1
"""

def binary_search(arr, search_item):
    start = 0
    end = len(arr)-1
    while start<=end:
        pivot = (start+end)//2
        if arr[pivot]==search_item:
            return pivot
        elif arr[pivot]>search_item:
            end = pivot-1
        else:
            start = pivot+1
    return -1
        


if __name__=="__main__":
    print(binary_search([1,2,3,4,5],2))
    print(binary_search([1,2,3,4,5],3))
    print(binary_search([1,2,3,4,5],5))
    print(binary_search([1,2,3,4,5],6))
    print(binary_search([5,6,10,13,14,18,30,34,35,37,40,44,64,79],10))
