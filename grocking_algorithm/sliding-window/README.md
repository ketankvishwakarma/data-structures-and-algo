# Problam Statement: Maximum sum of subarray of k size

Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].


# Solution

A basic brute force solution will be to calculate the sum of all ‘k’ sized subarrays of the given array to find the subarray with the highest sum. We can start from every index of the given array and add the next ‘k’ elements to find the subarray’s sum. Following is the visual representation of this algorithm for Example-1:

If you observe closely, you will realize that to calculate the sum of a contiguous subarray, we can utilize the sum of the previous subarray. For this, consider each subarray as a Sliding Window of size ‘k.’ To calculate the sum of the next subarray, we need to slide the window ahead by one element. So to slide the window forward and calculate the sum of the new position of the sliding window, we need to do two things:

Subtract the element going out of the sliding window, i.e., subtract the first element of the window.
Add the new element getting included in the sliding window, i.e., the element coming right after the end of the window.
This approach will save us from re-calculating the sum of the overlapping part of the sliding window. Here is what our algorithm will look like:

![Alt text](../images/01_maximum_sum_of_subarray_of_size_k.png?raw=true "Title")



# Problam Statement: Smallest Subarray With a Greater Sum

Given an array of positive numbers and a positive value `X`, what is the length of the smallest contiguous subarray whose sum is greater than or equal to `X`. Return 0 if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], X=7 
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], X=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: [3, 4, 1, 1, 6], X=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] 
or [1, 1, 6].

# Solution
- First we beign with the first element in the array.
- We mantain both start & end index (2 Pointer) and consider this as initial sum
  - Here we have a window of size 1
- If the current sum < X we slid i.e. we increase our sub array size which is now 2
- We keep increasing until window_sum >=X 
- If the window_sum > X we shrik i.e. we shift left pointer towards right. 
- we keep doing the same until we reach the end of array.

![Alt text](../images/02_smallest_subarray_with_greater_sum.png?raw=true "Title")