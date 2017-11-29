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