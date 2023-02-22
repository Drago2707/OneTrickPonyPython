"""Search Insert Position
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index 
where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        # if target < min(nums):
        #     temp = nums[0]
        #     while (temp) - 1 !
        if target > nums[-1]:
            num = nums[-1]
            fake_index = nums.index(num)
            while target > num:
                num += 1
                fake_index += 1
            return fake_index


print(Solution().searchInsert([1, 2, 3, 4, 5], 6))
