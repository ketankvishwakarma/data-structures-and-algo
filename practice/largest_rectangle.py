"""
Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.

There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by . If you join  adjacent buildings, they will form a solid rectangle of area .

Example

A rectangle of height h=2 and length k=3 can be constructed within the boundaries. The area formed is h*k = 2*3 =6.

Function Description

Complete the function largestRectangle int the editor below. It should return an integer representing the largest rectangle that can be formed within the bounds of consecutive buildings.

largestRectangle has the following parameter(s):

int h[n]: the building heights
Returns
- long: the area of the largest rectangle that can be formed within the bounds of consecutive buildings

Input Format

The first line contains , the number of buildings.
The second line contains  space-separated integers, each the height of a building.

Constraints

Sample Input

STDIN       Function
-----       --------
5           h[] size n = 5
1 2 3 4 5   h = [1, 2, 3, 4, 5]
Sample Output

9
Explanation

An illustration of the test case follows.
image

"""


def largest_house_optimized(h):
    h += [0]
    stack = []
    max_area = 0
    top = -1
    value = 0
    for i in range(len(h)):
        j = i
        current_val = h[i]
        while stack and stack[top][value] >= current_val:
            val, j = stack.pop()
            max_area = max(max_area, (i - j) * val)
        stack.append([h[i], j])
    return max_area

def largest_rectangle_bf(h):
    area = 0
    for i in range(len(h)):
        j = i
        w = 0
        hight = h[i]
        while(j < len(h)):
            if hight <= h[j]:
                w+=1
                j+=1
            else:
                hight = h[j]
        area = max(area,hight * w)
    return area


#print(largest_house([1,2,3,4,5]))
print(largest_house_optimized([10,5,20,30,5,20,10]))

print(largest_rectangle_bf([10,5,20,30,5,20,10]))

print(largest_house_optimized([11,11,10,10,10]))

print(largest_rectangle_bf([11,11,10,10,10]))