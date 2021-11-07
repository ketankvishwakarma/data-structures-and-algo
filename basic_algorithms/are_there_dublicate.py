"""
Implement a function called are_there_duplicates which accepts a variable 
number of argunment & checks whether there are any dublicates among the argunment passed in.

Example:

1,2,3   -> False
1,2,2   -> True
a,b,c,a -> True
"""

def dublicate(array):
    return len(set(array))!=len(array)

if __name__ =="__main__":
    print("[1,2,3]            {}".format(dublicate([1,2,3])))
    print("[1,2,2]            {}".format(dublicate([1,2,2])))
    print("['a','b','c','a']  {}".format(dublicate(['a','b','c','a'])))