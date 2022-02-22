"""
Write a recursive function called binary_search which accepts a sorted array and a value & returns the index
at which the value exists otherwise return -1
"""

def binary_search_recursive(item_list,item,start,end):
    if start == None:
        start = 0
    if end == None:
        end = len(item_list)-1
    if end >= start:
        mid = (start+end)//2
        if item_list[mid]==item:
            return mid
        elif item_list[mid] > item:
            return binary_search_recursive(item_list,item,start,mid-1)
        else:
            return binary_search_recursive(item_list,item,mid+1,end)
    else:
        return -1
    

if __name__ == "__main__":
    print(binary_search_recursive([1,2,3,4,5],5,None,None))
    print(binary_search_recursive([1,2,3,4,5],2,None,None))
    print(binary_search_recursive([1,2,3,4,5],3,None,None))
    print(binary_search_recursive([1,2,3,4,5],5,None,None))
    print(binary_search_recursive([1,2,3,4,5],6,None,None))
    print(binary_search_recursive([5,6,10,13,14,18,30,34,35,37,40,44,64,79],10,None,None))