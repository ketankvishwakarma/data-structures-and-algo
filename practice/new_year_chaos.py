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
    m = 0
    Q = [i-1 for i in q]
    print(q)
    print(Q)
    for i,j in enumerate(Q):
        if j-i > 2:
            print('Too chaotic')
            return
        for k in range(max(j-1, 0), i):
            if Q[k] > j:
                m += 1
    print(m)






if __name__=="__main__":
#    minimumBribes([1,2,3,5,4,6,7,8])
#    minimumBribes([2,1,5,3,4])
#    minimumBribes([2,5,1,3,4])
     #minimumBribes([1, 2, 5, 3, 4, 7, 8, 6])
     (minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]))


"""

[1, 2, 5, 3, 7, 8, 6, 4] 

[1, 2, 3, 7, 5, 8, 6, 4] = 2
       ^              ^
[1, 2, 3, 7, 5, 4, 6, 8] = 2 
          ^        ^
[1, 2, 3, 4, 5, 7, 6, 8] = 2 
             ^     ^     
[1, 2, 3, 4, 5, 6, 7, 8] = 1
             ^  ^

=============================
[1, 2, 5, 3, 4, 7, 8, 6]

[1, 2, 5, 3, 4, 7, 8, 6] = 0
 ^                    ^
[1, 2, 5, 3, 4, 7, 8, 6] = 0
    ^                 ^
[1, 2, 3, 4, 5, 7, 8, 6] = 2
       ^              ^
[1, 2, 3, 4, 5, 7, 8, 6] = 0
          ^           ^
[1, 2, 3, 4, 5, 7, 8, 6] = 0
             ^        ^
[1, 2, 3, 4, 5, 6, 7  8] = 1
                ^     ^
[1, 2, 3, 4, 5, 6, 7  8] = 0
                   ^  ^
[1, 2, 3, 4, 5, 6, 7  8] = 0
                      ^
                      ^ 
"""