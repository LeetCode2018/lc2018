"""
004. Median of Two Sorted Arrays - Hard
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


"""
13. Roman to Integer - Easy
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanMap = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        ret = romanMap[s[-1]] #the last one always add into value
        for i in range(0, len(s)-1):
            if romanMap[s[i]] < romanMap[s[i+1]]: #if one letter smaller than later, subtract
                ret -= romanMap[s[i]]
            else: #if one letter biger than later, add
                ret += romanMap[s[i]]
        return ret