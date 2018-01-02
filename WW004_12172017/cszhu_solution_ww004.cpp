/*============================
Easy:    028/035/038
============================*/
/*************************************************
28. Implement strStr()
**************************************************/
/*
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
*/

class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.size()>haystack.size()) return -1;
        for(int i=0;i<=haystack.size()-needle.size();i++)
        {
            if(haystack.substr(i, needle.size())==needle) return i;
        }
        return -1;
    }
};

/*************************************************
35. Search Insert Position
**************************************************/

/*Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

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
*/
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while(left < right)
        {
            int mid = left + (right-left)/2;
            if(nums[mid] < target) left = mid+1;
            else right = mid;
        }
        return left;
    }
};


/*************************************************
38. Count and Say
**************************************************/
/*The count-and-say sequence is the sequence of integers with the first five terms as following:

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
*/
class Solution {
public:
    string countAndSay(int n) {
        if(n<=0) return "";
        string res="1";
        for(int i=1;i<n;i++)
        {
           string tmp="";
           res.push_back('*');
           int count=0;
           for(int j=0;j<res.size();j++)
           {
               if(j!=0&&res[j]!=res[j-1])
               {
                   tmp.push_back(count+'0');
                   tmp.push_back(res[j-1]);
                   count=1;
               }
               else
               {
                   count++;
               }
           }
           res=tmp;
        }
        return res;
    }
};

============================
Medium:  022/024/029/031/033
============================
/*************************************************
22. Generate Parentheses
**************************************************/
/*Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
*/

//DFS Solution
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string path;
        helper(res, path, n, n);
        return res;
    }
    void helper(vector<string> &res, string path, int left, int right)
    {
       if(left==0&&right==0)
       {
          res.push_back(path);
          return;
       }
       if(left>right) return;
       if(left>0)
           helper(res, path+"(", left-1,right);
       if(right>0)
           helper(res, path+")", left, right-1);
    }
};


/*************************************************
24. Swap Nodes in Pairs
**************************************************/
/*Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
*/

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
       ListNode dummy(-1);
       dummy.next=head;
       ListNode *prev=&dummy;
       ListNode *cur=head;
       while(cur&&cur->next)
       {
          ListNode *tmp=cur->next->next;
          prev->next=cur->next;
          cur->next->next=cur;
          prev=cur;
          cur->next=tmp;
          cur=tmp;
       }
       return dummy.next;
    }
};
/*************************************************
29. Divide Two Integers
**************************************************/
/*Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
*/


class Solution {
public:
    int divide(int dividend, int divisor) {
        if (divisor == 0 || (dividend == INT_MIN && divisor == -1)) return INT_MAX;
        long long res=0;
        int sign=1;
        if((dividend<0&&divisor>0)||(dividend>0&&divisor<0)) sign=-1;
        long long m=abs((long long) dividend);
        long long n=abs((long long) divisor);
 
        while(m>=n)
        {
            long long t=n,p=1;
            while(m>=(t<<1))
            {
                t=t<<1;
                p=p<<1;
             
            }
            res+=p;
            m-=t;
        }
        return res==0?0:sign*res;
    }
};
/*************************************************
31. Next Permutation
**************************************************/
/*Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
*/
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if(nums.size()==1) return;
        int p_index=-1;
        for(int i=nums.size()-2;i>=0;i--)
        {
            if(nums[i]<nums[i+1]) {p_index=i;break;}
        }
        if(p_index!=-1)
        {
            for(int i=nums.size()-1;i>=0;i--)
            {
                if(nums[i]>nums[p_index]){swap(nums[i], nums[p_index]);break;}
            }
        }
        
        for(int left=p_index+1,right=nums.size()-1;left<right;)
            swap(nums[left++], nums[right--]);
    }
};

/*************************************************
33. Search in Rotated Sorted Array
**************************************************/
/*Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
*/

class Solution {
public:
    int search(vector<int>& nums, int target) {
        if(nums.size()==0) return -1;
        int left=0,right=nums.size()-1;
        while(left<=right)
        {
            int mid=left+(right-left)/2;
            if(nums[mid]==target) return mid;         
            else if(nums[mid]<nums[right])
            {
                if(nums[mid]<target&&nums[right]>=target) left=mid+1;
                else right=mid-1;
            }
            else
            {
                if(nums[left]<=target&&nums[mid]>target)right=mid-1;
                else left=mid+1;
            }
        }
        return -1;
        
    }
};

============================
Hard:    030/032
============================
/*************************************************
30. Substring with Concatenation of All Words
**************************************************/
/*
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
*/


class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> res;
        if(s.size()==0||words.size()==0) return res;
        int m=words.size(), len=words[0].size();
        if(s.size()<m*len) return res;
        map<string, int> m1;
        for(auto w:words)m1[w]++;
        for(int i=0;i<=s.size()-m*len;i++)
        {
            map<string, int> m2;
            for(int j=i;j<i+m*len;j+=len)
            {
                string tmp=s.substr(j, len);
                if(m1.find(tmp)==m1.end()) break;
                m2[tmp]++;
            }
            if(m2==m1) res.push_back(i);
        }
        return res;
    }
};

/*************************************************
32. Longest Valid Parentheses
**************************************************/
/*Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
*/

class Solution {
public:
    int longestValidParentheses(string s) {
        if(s.size()==0) return 0;
        stack<int> stk;
        stk.push(-1);
        int res=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]==')'&&s[stk.top()]=='(')
            {
                stk.pop();
                res=max(res, i-stk.top());
            }
            else
            {
                stk.push(i);
            }
        }
        return res;
        
    }
};
