"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from 1 to n.
Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

Example


q = [1,2,3,5,4,6,7,8]
If person 5 bribes person 4, the queue will look like this:
    [1,2,3,4,5,6,7,8]
Only  bribe is required. Print 1.

q = [4,1,2,3]
Person 4 had to bribe 3 people to get to the current position. Print `Too chaotic`.


"""

def minimumBribes(q):
    total_swaps = 0
    swap_count = {}
    for id in range(0,len(q)-1):
        x = q[id]>q[id+1]
        print("{} > {} {}".format(q[id],q[id+1],x))
        if q[id]>q[id+1]:
            temp = q[id]
            q[id] = q[id+1]
            q[id+1] = temp 
            if q[id+1] in swap_count.keys():
                count = swap_count.get(q[id+1])
                if count >= 2:
                    print("Too chaotic.")
                    return
                else:
                    swap_count[q[id+1]] = count+1
            else:
                swap_count[q[id+1]] = 1
            total_swaps=total_swaps+1
    print(total_swaps)
    print(swap_count)
    print(q)
    


    




if __name__=="__main__":
#    minimumBribes([1,2,3,5,4,6,7,8])
#    minimumBribes([2,1,5,3,4])
#    minimumBribes([2,5,1,3,4])
     minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])