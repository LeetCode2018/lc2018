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
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #The median is either n//2 for odd, or (n//2+n//2-1)/2 for even
        lenA, lenB = len(nums1), len(nums2) #n=lenA+lenB
        if lenA==0 and lenB==0:
            return None
        i = j = curr = 0
        mid1 = mid2 = 0 #mid1 for the n//2-1 number, mid2 for the n//2 number
        while (i+j < lenA+lenB):
            if i >= lenA or (j < lenB and nums1[i] >= nums2[j]):
                curr = nums2[j]
                j += 1
            elif j >= lenB or (i < lenA and nums1[i] < nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                print("ERROR!")
                return None

            if i+j-1 == (lenA+lenB)//2-1:
                mid1 = curr
            if i+j-1 == (lenA+lenB)//2:
                mid2 = curr
                break;

        if (lenA+lenB) & 1:#odd
            return mid2
        else:#even
            return (mid1+mid2)/2

"""
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        For each char, check with two directions (left and right) at same time
        consider ood: "aba", and even: "abba"
        '''
        res = ""
        for i in range(len(s)):
            # odd
            tmp = self.getLongestPal(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even
            tmp = self.getLongestPal(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def getLongestPal(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

"""
006. ZigZag Conversion 
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        '''
        Use numRows lists sLine to scan s, put each line into sLine[row]
        '''
        sLine = [''] * numRows
        ret = ""

        if numRows <= 1 or len(s) < numRows:
            return s
        row, direction = 0, 1
        for c in s:
            sLine[row] += c
            if row == numRows-1:
                direction = -1
            elif row == 0:
                direction = 1
            row += direction

        for i in range(numRows):
            ret += sLine[i]

        return ret

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