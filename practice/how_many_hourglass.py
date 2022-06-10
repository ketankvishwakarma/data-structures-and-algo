"""
An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g


1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

There are 16 hourglasses in Array . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .


Sample Input 

-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0


 -63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18

The highest hourglass sum is 28 from the hourglass beginning at row , column :
0 4 3
  1
8 6 6


Sample Output: 19


The hourglass with the maximum sum () is:

2 4 4
  2
1 2 4
"""