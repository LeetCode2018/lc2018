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

"""
16. 3Sum Closest
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closestSum = 0
        currSum, currGap, minGap = 0, 0, sys.maxsize
        if not nums or len(nums) < 3:
            return 0
        nums.sort()
        for i in range(len(nums)-2):
            l, r = i + 1, len(nums)-1
            while l < r:
                currSum = nums[i]+nums[l]+nums[r]
                currGap = abs(currSum-target)
                if currGap < minGap:
                    minGap = currGap
                    closestSum = currSum
                if currSum > target:
                    r -= 1
                elif currSum < target:
                    l += 1
                else: #currSum == target
                    return target
        return closestSum

"""
17. Letter Combinations of a Phone Number
Given a digit string, return all possible letter combinations that the number could represent.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digitMap = { '1': '',    '2': 'abc', '3': 'def',
                     '4': 'ghi', '5': 'jkl', '6': 'mno',
                     '7': 'pqrs','8': 'tuv', '9': 'wxyz',
                     '0': ' '}
        ret = [''] if digits else []
        for d in digits:
            ret = [item+append for append in digitMap[d] for item in ret]
        
        return ret
"""
18. 4Sum
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) < 4:
            return []
        Ret = []
        self.nSum(nums, target, 4, [], Ret)
        return Ret

    def nSum(self, nums, target, n, lastRet, Ret):
        if n > len(nums) or n < 2:
            return
        if n == 2:
            l,r = 0,len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    Ret.append(lastRet + [nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif s > target: r -= 1
                else: l += 1
        else:
            for i in range(0, len(nums)-n+1):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                else:
                    self.nSum(nums[i+1:], target-nums[i], n-1, lastRet+[nums[i]], Ret)
        return

"""
19. Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        '''
        Define two markers, 2nd marker come after 1st behind n
        '''
        second = first = head
        iLoop = 0
        if not head:
            return Null
        while first and iLoop < n:
            first = first.next
            iLoop += 1
        #handle the special case
        if not first:
            return head.next
        while first.next:
            first = first.next
            second = second.next
        if second:
            second.next = second.next.next
        return head

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
23. Merge k Sorted Lists
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        """
        Time complexity: O(N*logN)
        """
        sortedArray = []
        sortedHead = ListNode(0)
        currNode = sortedHead
        for head in lists:
            while head:
                sortedArray.append((head.val, head))
                head = head.next
        sortedArray.sort(key=lambda tup: tup[0])#TODO: lambda usage
        for node in sortedArray:
            currNode.next = node[1]
            currNode = currNode.next
        return sortedHead.next
        
"""
25. Reverse Nodes in k-Group
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        '''
        reverse the list between start and end, then connect: previous -> start -> end -> afterward
        '''
        dummy = jump = ListNode(0)
        l = r = head
        dummy.next = head
        
        while 1:
            iLoop = 0
            while iLoop < k and r:
                r = r.next
                iLoop += 1
            if iLoop == k:
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  #TODO: standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next

"""
26. Remove Duplicates from Sorted Array
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        endIdx = 0
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[endIdx]:
                endIdx += 1
                nums[endIdx] = nums[i]
                
        return endIdx + 1

"""
27. Remove Element
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        endIdx = 0
        for num in nums:
            if num != val:
                nums[endIdx] = num
                endIdx += 1
        return endIdx