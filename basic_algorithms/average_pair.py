"""
Wirte a function called average_pair. Given a sorted array of integers and a 
target average, determine if there is a pair of values in the array where the 
average of the pair equals the target average. There may be more than one pair
that matches the avaerage target.

average_pair([1,2,3],2.5) --> True
average_pair([1,3,3,5,6,7,10,12,19],8) --> True
average_pair([-1,0,3,4,5,6],4.1) --> False
average_pair([],4) --> False
"""

def average_pair(array, target):
    left = 0
    right = len(array)-1
    while left < right:
        temp_avg = array[left]+array[right] / 2
        #print(" {} / {} = {}".format(array[left],array[right],temp_avg))
        if temp_avg == target:
            return True
        if temp_avg < target:
            left = left + 1
        else:
            right= right - 1
    return False

    

if __name__ == "__main__":
    print("[1,2,3],2.5 --> {}".format(average_pair([1,2,3],2.5)))
    print("[1,3,3,5,6,7,10,12,19],8 --> {}".format(average_pair([1,3,3,5,6,7,10,12,19],8)))
    print("[],4 --> {}".format(average_pair([],4)))
    print("[-1,0,3,4,5,6],4.1 --> {}".format(average_pair([],4)))