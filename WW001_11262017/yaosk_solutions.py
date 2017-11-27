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

        """O(n) solution, """
        if len(nums) <= 1:
            return false
        sumdict = {}
        for index item in enumerate(nums):
            if (target - item) in sumdict:
                return [sumdict[target - item], index]
            else:
                sumdict[item] = index

"""
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit
 signed integer range. For the purpose of this problem, assume that your function returns 
 0 when the reversed integer overflows.
"""
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        Another short and nice python solution:
        s = cmp(x, 0) #signal indicator
        r = int(`s*x`[::-1]) #revese string
        return s*r * (r < 2**31) #get negtive signal
        """
        ret = temp = 0;
        temp = abs(x);
        while temp:
            ret *= 10;
            ret += temp % 10;
            temp = int(temp/10);

        if x < 0:
            ret = -ret;
        if ret > 2147483647 or ret < -2147483648:
            ret = 0;
        return ret;

"""
9. Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.
Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        reversex = 0
        temp = x
        while temp:
            reversex *= 10
            reversex += temp%10
            temp = int(temp/10)
        return reversex == x

"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rootlist = currlist = ListNode(0);
        carry = 0;
        while l1 or l2 or carry:
            if l1:
                l1val = l1.val;
                l1 = l1.next;
            else:
                l1val = 0;

            if l2:
                l2val = l2.val;
                l2 = l2.next;
            else:
                l2val = 0;

            currlist.next = ListNode((carry + l1val + l2val) % 10);
            currlist = currlist.next;
            """//10 is roundness of /10"""
            carry = (carry + l1val + l2val) // 10;

        return rootlist.next;


"""
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        1. O(n^2)
           For each character, search current substring for duplicate,
           if yes: get current longest length, and start over with that duplicated char in substring;
           if no: current longest length + 1.
        2. O(n)
           Use a hash map for all char and index of current substring, so the process of search current substring can be O(1)
        3. O(n)
           Another O(n) idea is use a fixed list (ASCII table size: 128), which will help to reduce map size
           to indicate existing of each character
        """
        maxLen = startIdx = 0;
        charDict = {};
        for i in range(len(s)):
            if s[i] in charDict:
                startIdx = max(charDict[s[i]] + 1, startIdx); #Met bug here, consider the case startIdx go back, fox ex: abba
                if (i - startIdx + 1) > maxLen:
                    maxLen = i - startIdx + 1;
            else:
                maxLen = max(maxLen, i - startIdx + 1);
            charDict[s[i]] = i;

        return maxLen;

