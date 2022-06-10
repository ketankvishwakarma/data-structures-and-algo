"""
Link: https://leetcode.com/problems/first-bad-version/

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1

"""
import random

class Solution:
    def firstBadVersion(self, n: int) -> int:
        nums = list(range(1,n+1))
        print(nums)
        bad = random.choice(nums)
        start = 0
        end = len(nums)
        while start<=end:
            mid = int((start+end)/2)
            isBadVersion(nums[mid])
            if isBadVersion(nums[mid]):
                
                return mid
            elif target > nums[mid]:
                start=mid+1
            else:
                end=mid-1
        return -1


if __name__ =="__main__":
    s = Solution()
    s.firstBadVersion(10)
