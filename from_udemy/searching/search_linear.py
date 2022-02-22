"""
Implement linear search
"""

def linear_search(arr,item):
    for index,x in enumerate(arr):
        if x == item:
            return index
    return -1

if __name__ == "__main__":
    print(linear_search([10,15,20,25,30],15))
    print(linear_search([9,8,7,6,5,4,3,2,1,0],4))
    print(linear_search([100],100))
    print(linear_search([1,2,3,4,5],6))
    print(linear_search([9,8,7,6,5,4,3,2,0],10))
    print(linear_search([100],200))