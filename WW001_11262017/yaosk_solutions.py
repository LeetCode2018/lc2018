"""
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """"O(n^2) solution: exceed time limit"""
        """
        for indexi, i in enumerate(nums):
            for indexj, j in enumerate(nums[indexi+1:]):
                if i+j == target:
                    return [indexi, indexi+indexj+1]
        """
        
        """O(n) solution"""
        if len(nums) <= 1:
            return false
        sumdict = {}
        for i in range(len(nums)):
            if target - nums[i] in sumdict:
                return [sumdict[target - nums[i]], i]
            else:
                sumdict[nums[i]] = i

"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


