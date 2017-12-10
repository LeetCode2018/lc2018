/*============================
Easy:   021/026/027
============================*/
/*************************************************
021. Merge Two Sorted List
**************************************************/

/*
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        priority_queue<pair<int, ListNode*>, vector<pair<int, ListNode*>>, greater<pair<int, ListNode*> > > pq;
        if(l1) pq.push({l1->val, l1});
        if(l2) pq.push({l2->val, l2});
        ListNode dummy(-1);
        ListNode *prev=&dummy;
        while(!pq.empty())
        {
            auto p=pq.top();pq.pop();
            prev->next=p.second;
            prev=prev->next;
            if(p.second->next!=NULL) pq.push({p.second->next->val, p.second->next});
        }
        return dummy.next;
        
    }
};

/*************************************************
026.Remove Duplicates from Sorted Array
**************************************************/

Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.


/*************************************************
027.Remove Elements
**************************************************/
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.


============================
Medium: 015/016/017/018/019
============================
/*************************************************
015. 3 Sum
**************************************************/
/*
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
*/
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if(nums.size()<3) return {};
        int m=nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int> > res;
        for(int i=0;i<=m-2;i++)
        {
            if(nums[i]>0) break;
            if(i>0&&nums[i]==nums[i-1]) continue;
            int left=i+1, right=m-1;
            int target=0-nums[i];
            while(left<right)
            {
                if(nums[left]+nums[right]==target)
                {
                    res.push_back({nums[i],nums[left], nums[right]});
                    while(left<right&&nums[left+1]==nums[left]) left++;
                    while(left<right&&nums[right-1]==nums[right])right--;
                    left++;
                    right--;
                }
                else if(nums[left]+nums[right]<target) left++;
                else right--;
            }
        }
        return res;
        
    }
};
/*************************************************
016. 3 Sum Cloest
**************************************************/
/*Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
*/

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        if(nums.size()<3) return 0;
        int res=nums[0]+nums[1]+nums[2];
        sort(nums.begin(), nums.end());
        for(int k=0;k<nums.size()-2;k++)
        {
            if(k!=0&&nums[k]==nums[k-1]) continue;
            int i=k+1,j=nums.size()-1;
            while(i<j)
            {
                int sums=nums[i]+nums[j]+nums[k];
                if(sums==target) return sums;
                res=(abs(sums-target)<abs(res-target)?sums:res);
                if(sums>target)--j;
                else ++i;
            }
        }
        return res;
   }
};

/*************************************************
017. Letter Combinations of a Phone Number
**************************************************/
/*
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
*/
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<vector<char> > dict={{}, {}, {'a', 'b', 'c'},{'d','e','f'},{'g','h','i'},{'j', 'k', 'l'},
                                    {'m', 'n', 'o'}, {'p', 'q', 'r', 's'}, {'t', 'u', 'v'}, {'w', 'x', 'y', 'z'}};
        vector<string> res;
        if(digits.size()==0) return {};
        string path="";
        helper(digits, 0, res, path, dict);
        return res;
        
    }
    void helper(string digits, int start, vector<string> &res, string path, vector<vector<char>>&dict)
    {
        if(start==digits.size())
        {
            res.push_back(path);
            return;
        }
       
            for(auto c:dict[digits[start]-'0'])
            {
                helper(digits, start+1, res, path+c, dict);
            }
    }
};

/*************************************************
018. 4 Sum
**************************************************/
/*
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
*/

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int> > res;
        if(nums.size()<4) return res;
        sort(nums.begin(), nums.end());
        for(int i=0;i<=nums.size()-4;i++)
        {
            if(i!=0&&nums[i]==nums[i-1]) continue;
            for(int j=i+1;j<=nums.size()-3;j++)
            {
                if(j!=i+1&&nums[j]==nums[j-1]) continue;
                for(int k=j+1;k<=nums.size()-2;k++)
                {
                    if(k!=j+1&&nums[k]==nums[k-1]) continue;
                    int l=k+1, r=nums.size()-1;
                    int t=target-nums[i]-nums[j]-nums[k];
                    while(l<=r)
                    {
                       int mid=l+(r-l)/2;
                       if(nums[mid]==t)
                       {
                           res.push_back({nums[i], nums[j], nums[k], nums[mid]});
                           break;
                       }
                       else if(nums[mid]>t)
                       {
                           r=mid-1;
                       }
                       else
                       {
                           l=mid+1;
                       }
                    }  
                }
            }
        }
        return res;
    }
};


/*************************************************
019. Remove Nth Node From End of List
**************************************************/
/*Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head==NULL) return NULL;
        ListNode dummy(-1);
        dummy.next=head;
        ListNode *prev=&dummy;
        ListNode *fast=head;
        for(int i=0;i<n;i++)
            fast=fast->next;
        ListNode *slow=head;
        while(fast)
        {
            fast=fast->next;
            prev=slow;
            slow=slow->next;
        }
        prev->next=slow->next;
        return dummy.next;
    }
};

============================
Hard:   023/025
=
/*************************************************
023. Merge K Sorted Lists
**************************************************/

/*Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        struct comp{
          bool operator()(pair<int, ListNode*>&a, pair<int, ListNode*>&b)
          {
              return a.first>b.first;
          }
        };
        priority_queue<pair<int, ListNode*>, vector<pair<int, ListNode*>>, comp> pq;
        for(auto l:lists)
        {
            if(l) pq.push({l->val, l});
        }
        ListNode dummy(-1);
        ListNode *prev=&dummy;
        while(!pq.empty())
        {
            auto a=pq.top();pq.pop();
            prev->next=a.second;
            prev=prev->next;
            if(a.second->next) pq.push({a.second->next->val, a.second->next});
        }
        return dummy.next;
    }
};

/*************************************************
025. Reverse Nodes in k-Group
**************************************************/
/*
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(head==NULL&&k<=1)return head;
        ListNode dummy(-1);
        ListNode *prev=&dummy;
        prev->next=head;
        ListNode *start=head;
        int cnt=0;
        ListNode *cur=head;
        while(cur)
        {
            cnt++;
            if(cnt==k)
            {
                ListNode *tmp=cur->next;
                cur->next=NULL;
                ListNode *node=reverse(start);
                prev->next=node;
                prev=start;
                start->next=tmp;
                start=tmp;
                cur=tmp;
                cnt=0;
            }
            else
            {
                cur=cur->next;
            }
        }
        return dummy.next;
        
    }
    ListNode *reverse(ListNode* head)
    {
        ListNode *prev=NULL;
        while(head)
        {
            ListNode *tmp=head->next;
            head->next=prev;
            prev=head;
            head=tmp;
        }
        return prev;
    }
};
