"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        if n == 0:
            return [""]
        self.dfs(n, n, ret, "")
        return ret

    def dfs(self, l, r, ret, last):
        if l == 0 and r == 0: #got a valid result, append into list
            ret.append(last)
            return
        if l > r: #invalid answer, just return
            return
        if l > 0:
            self.dfs(l-1, r, ret, last+"(")
        if r > 0:
            self.dfs(l, r-1, ret, last+")")

"""
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''p0->p1->p2'''
        p1 = ret = ListNode(0)
        ret.next = head
        p1.next = head
        if not head:
            return head

        while p1.next and p1.next.next:
            p0, p1, p2 = p1, p1.next, p1.next.next
            p0.next, p1.next, p2.next = p2, p2.next, p1

        return ret.next
        
"""
28. Implement strStr()
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            if (haystack[i:i+len(needle)] == needle):
                return i
        return -1

"""
29. Divide Two Integers
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return pow(2,31)-1
        abs_dividend, abs_divisor = abs(dividend), abs(divisor)
        ret = 0
        """
        while abs_dividend >= abs_divisor:
            abs_dividend -= abs_divisor
            ret += 1
        """
        '''
        Use bit shift to accelerate
        '''
        while abs_dividend >= abs_divisor:
            acc_divisor, i = abs_divisor, 1
            while abs_dividend >= acc_divisor:
                abs_dividend -= acc_divisor
                ret += i
                acc_divisor <<= 1
                i <<= 1

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            ret = -1 * ret
        
        if ret < -pow(2,31) or ret > pow(2,31)-1:
            ret = pow(2,31)-1
        return ret

"""
31. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        if len_nums < 2:
            return
        '''
        1. find the longest non-increse suffix
        '''
        right = len_nums - 1
        while nums[right] <= nums[right-1] and right-1 >= 0:
            right -= 1
        '''
        2. the pivot is the left one of this suffix
        '''
        pivot = right - 1
        if pivot < 0:
            return self.reverse(nums, 0, len_nums-1)
        '''
        3. reverse pivot with the most right one which is larger than pivot
        '''
        replacement = 0
        for i in range(len_nums-1, pivot, -1):
            if nums[i] > nums[pivot]:
                replacement = i
                break
        nums[pivot], nums[replacement] = nums[replacement], nums[pivot]
        '''
        4. reverse remaining suffix
        '''
        self.reverse(nums, pivot+1, len_nums-1)
        
    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1

"""
32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        stack, left, ret = [], -1, 0
        for i in range(len(s)):
            if s[i] == '(':#(
                stack.append(i)
            else:#)
                if not stack:#update left because last parentheses end
                    left = i
                else:
                    stack.pop()
                    if not stack:
                        ret = max(ret, i-left)
                    else:
                        ret = max(ret, i-stack[-1])
        return ret

"""
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''Can assume at least half of the list is sorted, log(N) based on that'''
        if not nums: return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = round((left + right) / 2)
            print(left, right, mid)
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]: #left part sorted, don't consider == because no duplicated number
                if nums[left] <= target <= nums[mid]: #target in [left...mid]
                    right = mid - 1
                else:
                    left = mid + 1
            else:#right part sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
            print(left, right)
        return -1

"""
35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 1:

Input: [1,3,5,6], 0
Output: 0
"""
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or nums[0] > target:
            return 0
        length = len(nums)
        if nums[-1] < target:
            return length
        l, r, m = 0, length-1, 0
        while l <= r:
            m = int((l+r)/2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
                if l >= length:
                    return length
                elif nums[l] > target:
                    return l
            elif nums[m] > target:
                r = m - 1
                if r < 0:
                    return 0
                elif nums[r] < target:
                    return r + 1

"""
38. Count and Say
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            count = 1
            temp = []
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index-1])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s