"""
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = curr = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if not l1:
            curr.next = l2
        if not l2:
            curr.next = l1

        return ret.next

"""
15. 3Sum
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #sort at first
        nums.sort()
        ret = []
        for i in range(len(nums)-2):
            #avoid duplicated solution
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            l,r = i+1,len(nums)-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0: r -= 1
                elif sum < 0: l += 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    #Skip the same item if any, ex. [-2,0,0,2,2]
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1] < r: r -= 1
                    l, r = l+1, r-1
        return ret
