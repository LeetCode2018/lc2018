/************
001. Two Sum
************/
/*Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        for(int i=0;i<nums.size();i++){
            if(m.count(target-nums[i])!=0) return { m[target-nums[i]], i};
            else m[nums[i]]=i;
        }
        return {-1, -1};
    }
};


/********************
007 Reverse Integer
********************/
/*Given a 32-bit signed integer, reverse digits of an integer.

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
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
*/
class Solution {
public:
    int reverse(int x) {
       int sign=(x>0?1:-1);
       x=sign*x;
       long long res=0;
       while(x){
           res=res*10+x%10;
           x=x/10;
       };
       res*=sign;
       return res>INT_MAX||res<INT_MIN?0:res;
    }
};



/***********************
009 Palindrome Number
************************/
/*Determine whether an integer is a palindrome. Do this without extra space.*/
class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return false;
        long long a=0;
        long long y=x;
        while(x){
           a=a*10+x%10;
           x=x/10;
        }
        return a==y;  
    }
};



/**********************
 002 Add Two Numbers
***********************/
/*You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(-1);
        ListNode *cur=&dummy;
        int carry=0;
        while(l1||l2){
            int n1=l1?l1->val:0;
            int n2=l2?l2->val:0;
            int val=n1+n2+carry;
            carry=val/10;
            val=val%10;
            cur->next=new ListNode(val);
            cur=cur->next;
            l1=l1?l1->next:l1;
            l2=l2?l2->next:l2;
        }
        if(carry)
            cur->next=new ListNode(carry);
        return dummy.next;
    }
};

/*************************************************
003 Longest Substring Without Repeating Characters  
**************************************************/
/*Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
*/
ass Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> m;
        int res=0;
        int left=0;
        for(int i=0;i<s.size();i++){
            if(m.count(s[i])!=0){
                left=max(left, m[s[i]]+1);
            res=max(res, i-left+1);
            m[s[i]]=i;
        }
        return res;
    }
};
