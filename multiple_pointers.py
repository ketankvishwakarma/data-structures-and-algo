"""
Implement a function called areThereDublicates which accept a variable umber of argunments
and check whether there are any duplicates amoung the argunments passed in.

areThereDuplicates(1,2,3) --> False
areThereDuplicates(1,2,2) --> True
areThereDuplicates(a,b,c,d) --> False
"""

def are_there_duplicates(arr):
    temp_dict = {}
    
    for value in arr:
        if value in temp_dict.keys():
            temp_dict.update({value:temp_dict.get(value)+1})
        else:
            temp_dict.update({value:1})
    for key in temp_dict.keys():
        if temp_dict[key] > 1:
            return False
    return True       
    

if __name__ == "__main__":
    print("[a,b,c,d,a] --> {}".format(are_there_duplicates(["a","b","c","d","a"])))
    print("[1,2,3] --> {}".format(are_there_duplicates([1,2,3])))
    print("[1,2,2] --> {}".format(are_there_duplicates([1,2,2])))