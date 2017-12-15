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
