/*============================
Easy: 	013/014/020
============================*/
/*************************************************
013. Roman to Integer
**************************************************/
/*Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.*/

class Solution {
public:
    int romanToInt(string s) {
        map<char, int> m;
        m['M']=1000;m['D']=500;m['C']=100;m['L']=50;m['X']=10;m['V']=5;m['I']=1;
        int res=0;
        for(int i=0;i<s.size();i++){
            if(i!=0&&m[s[i]]>m[s[i-1]]) res-=2*m[s[i-1]];
            res+=m[s[i]];
        }
        return res;
    }
};




/*************************************************
014. Longest Common Prefix
**************************************************/
/*Write a function to find the longest common prefix string amongst an array of strings.*/

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size()==0||strs[0].size()==0) return "";
        for(int i=0;i<strs[0].size();i++){
            for(int j=0;j<strs.size();j++){
                if(strs[j].size()<=i||strs[j][i]!=strs[0][i])
                    return strs[0].substr(0, i);
    }
    return strs[0];
};



/*************************************************
020. Valid Parentheses
**************************************************/
/*Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.*/

class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for(int i=0;i<s.size();i++){
           if((s[i]=='}'&&(stk.empt()||stk.top()!='{'))||
              (s[i]=='}'&&(stk.empt()||stk.top()!='{'))||
              (s[i]=='}'&&(stk.empt()||stk.top()!='{')))
              return false;
           else if(s[i]=='{'||s[i]=='('||s[i]=='[')
              stk.push(s[i]);
           else
              stk.pop();
        }
        return true;  
    }
};




/*============================
Medium:	005/006/008/011/012
============================*/
/*************************************************
 005. Longest Palindromic Substring
**************************************************/
/*Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
*/

class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size()==0) return "";
        int m=s.size();
        int len=1, idx=0;
        vector<vector<int> > dp(m, vector<int> (m, false));
        for(int i=0;i<m;i++){
            dp[i][i]=true;
            for(int j=0;j<i;j++){
               if(s[i]==s[j]&&(i-j<2||dp[j+1][i-1])){
                  dp[j][i]=true;
                  if(i-j+1>len){
                      len = i-j+1;
                      idx = j;
                  }
               }
            }
         }
         return s.substr(idx, len);   
    }
};

/*************************************************
006. ZigZag Conversion 
**************************************************/
/*The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
*/

class Solution {
public:
    string convert(string s, int numRows) {
      if(s.size()<=numRows||numRows==1)  return s;
      string res="";
      for(int i=0;i<numRows; i++){
          int j=i;
          while(j<s.size()){
              res.push_back(s[j]);
              if(i!=0&&i!=numRows-1&&(j+2*numRows-2-2*i)<s.size()){
                  res.push_back(s[j+2*numRows-2-2*i]);
              }
              j=j+2*numRows-2;
          }
      }
      return res;
    }
};

/*************************************************
008. String to Integer (atoi)
**************************************************/
/*Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
*/
class Solution {
public:
    int myAtoi(string str) {
        if(str.size()==0) return 0;
        int i=0;
        int m=str.size();
        int sign=1;
        while(i<m&&str[i]==' ') i++;
        if(str[i]=='+'||str[i]=='-') sign=(str[i++]=='+'?1:-1);
        int base=0;
        for(;i<m;i++){
            if(str[i]>'9'||str[i]<'0') break;
            if(base>INT_MAX/10||(base==INT_MAX/10&&str[i]>'7'))
                return sign==1?INT_MAX:INT_MIN;
            base=base*10+str[i]-'0';
        }
        return sign*base;   
    }
};


/*************************************************
011. Container With Most Water
**************************************************/
/*Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
*/
class Solution {
public:
    int maxArea(vector<int>& height) {
        if(height.size()==0) return 0;
        int res=0;
        int left=0, right=height.size()-1;
        while(left<right){
            res=max(res, min(height[left], height[right])*(right-left));
            if(height[left]>height[right]) right--;
            else left++;
        }
        return res;
    }
};


/*************************************************
012. Integer to Roman
**************************************************/
/*Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.*/

class Solution {
public:
    string intToRoman(int num) {
        string symbols[] ={"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int  radius[]  ={1000,900,500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        int index=0;
        string res="";
        while(num){
            int cnt=num/radius[index];
            for(int i=0;i<cnt;i++) res+=symbols[index];
            num-=radius[index]*cnt;
            index++;
        }
        return res;   
    }
};



============================
Hard:    004/010
============================
/*************************************************
004. Median of Two Sorted Arrays
**************************************************/
/*There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
*/

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m=nums1.size(), n=nums2.size();
        int k=(m+n)/2;
        int idx1 = 0, idx2 = 0;
        double a=0, b=0;
        for(int i=1;i<=k+1;i++){
            int val = idx1<m&&idx2<n?(nums1[idx1]>nums2[idx2]?nums2[idx2]:nums1[idx1]):((idx1<m)?nums1[idx1]:nums2[idx2]);
            if(i==k) a=val;
            if(i==k+1) b=val;
            idx1<m&&idx2<n?(val==nums1[idx1]?idx1++:idx2++):(idx1<m?idx1++:idx2++);
        }
        if((m+n)%2) return b;
        else return (a+b)/2;     
    }
};


/*************************************************
010. Regular Expression Matching
**************************************************/
/*
Implement regular expression matching with support for '.' and '*'.

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

*/

class Solution {
public:
    bool isMatch(string s, string p) {
        int m=s.size(), n=p.size();
        int dp[m+1][n+1];
        fill_n(&dp[0][0], (m+1)*(n+1), false);
        dp[0][0]=true;
        for(int i=0;i<=m;i++){
            for(int j=1;j<=n;j++){
                if(j>1&&p[j-1]=='*'){
                    dp[i][j]=dp[i][j-2]||(i>0&&dp[i-1][j]&&(s[i-1]==p[j-2]||p[j-2]=='.');
                else
                    dp[i][j]=i>0&&dp[i-1][j-1]&&(s[i-1]==p[i-1]||p[i-1]=='.')
            }
       }
       return dp[m][n];
    }
};
