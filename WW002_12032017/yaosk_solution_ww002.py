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
8. String to Integer (atoi)
Implement atoi to convert a string to an integer.
"""
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        '''
        No clear input string define!
        '''
        if len(str) == 0: return 0
        ret, i, sign = 0, 0, 1
        bMetNum = False
        str = str.strip()

        for i in range(len(str)):
            if str[i].isdigit():
                bMetNum = True
                ret = 10*ret + ord(str[i]) - 48 #ord('0') == 48
            elif str[i] == '-' and bMetNum == False:
                bMetNum = True
                sign = -1
            elif str[i] == '+' and bMetNum == False:
                bMetNum = True
                sign = 1
            elif bMetNum == True: #once meet number, don't accept any non-number character
                break
            else:
                return 0
        ret = max(-2147483648, min(2147483647, sign*ret))
        return ret
        
"""
10. Regular Expression Matching
mplement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(s)+1) for i in range(len(p)+1)] #+1 for the null string case
        dp[0][0] = True #s=p=""
        for i in range(2, len(p) + 1):#s="", p not null
            dp[i][0] = dp[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p)+1): #loop start with p because p is the one with regular
            for j in range(1, len(s)+1):
                if p[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i-2][j]#case a vs ab*
                    if p[i-2] == s[j-1] or p[i-2] == '.':
                        dp[i][j] |= dp[i][j-1]
                elif p[i-1] == '.' or p[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False

        return dp[-1][-1]

"""
11. Container With Most Water
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxContainer = minHeight = 0
        l, r = 0, len(height) - 1
        while l < r:
            minHeight = min(height[l], height[r])
            maxContainer = max(maxContainer,  minHeight * (r - l))
            l = l + (height[l] == minHeight)
            r = r - (height[r] == minHeight)
        return maxContainer
        
"""
12. Integer to Roman
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];

        m = math.floor(num/1000)
        c = math.floor((num%1000)/100)
        x = math.floor((num%100)/10)
        i = math.floor(num%10)
        return M[m] + C[c] + X[x] + I[i]

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
        
"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ""
        if not strs: return ret
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if not strs[j] or i >= len(strs[j]): return ret
                elif strs[j][i] != strs[0][i]:
                    return ret;
            ret += strs[0][i]
        return ret
        
"""
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftStr = rightStr = ""
        lastLeftStart = 0
        if not s: return True
        for i in range(len(s)):
            if self.isLeft(s[i]):
                leftStr += s[i]
            elif self.isRight(s[i]):
                if leftStr == "": return False
                elif not self.isMatch(leftStr[-1], s[i]):
                    return False
                else:
                    leftStr = leftStr[0:-1]
            else:
                return False

        return leftStr == ""
        
    def isMatch(self, l, r):
        if (l=='(' and r==')') or (l=='[' and r==']') or (l=='{' and r=='}'):
            return True
        else:
            return False

    def isRight(self, c):
        if c==')' or c==']' or c=='}':
            return True
        else:
            return False
    
    def isLeft(self, c):
        if c=='(' or c=='[' or c=='{':
            return True
        else:
            return False
