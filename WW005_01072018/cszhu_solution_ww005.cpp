/*============================
Easy:    053/058
============================*/
/*************************************************
53. Maximum Subarray
**************************************************/
/*Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
*/
class Solution {
public:
    int maxSubArray(vector<int> &nums){
        int n=nums.size();
        vector<int> dp(n, 0);
        dp[0]=nums[0];
        int mx=dp[0];
        for(int i=1;i<nums.size();i++)
        {
            dp[i]=nums[i]+(dp[i-1]>0?dp[i-1]:0);
            mx=max(mx, dp[i]);
        }
        return mx;
    }
};

/*************************************************
58. Length of Last Word
**************************************************/
/*Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
*/

class Solution {
public:
    int lengthOfLastWord(string s) {
        int start=-1;
        int end=-1;
        for(int i=s.size()-1;i>=0;i--)
        {
            if(s[i]!=' '&& end==-1)
            {
                end=i;
            }
            else if(end!=-1&&s[i]==' ')
            {
                start=i;
                break;
            }
        }
        return end-start;
    }
};

/*============================
Medium:    036/039/040
============================*/
/*************************************************
36. Valid Sudoku
**************************************************/
/*Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
*/

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        if(board.size()!=9||board[0].size()!=9) return false;

        //Check the rows
        for(int i=0;i<9;i++)
        {
            map<char, int> mp;
            for(int j=0;j<9;j++)
            {
                if(board[i][j]!='.'&&board[i][j]<'1'&&board[i][j]>'9') return false;
                if(board[i][j]!='.')
                {
                   mp[board[i][j]]++;
                   if(mp[board[i][j]]>1) return false;
                }
            }
        }
        //Check the col
        for(int j=0;j<9;j++)
        {
            map<char, int> mp;
            for(int i=0;i<9;i++)
            {
                if(board[i][j]!='.'&&board[i][j]<'1'&&board[i][j]>'9') return false;
                if(board[i][j]!='.')
                {
                   mp[board[i][j]]++;
                   if(mp[board[i][j]]>1) return false;
                }
            }
        }
        vector<vector<int> > dir ={{0,0}, {0, 3}, {0, 6},{3,0},{3,3}, {3,6},{6,0},{6,3},{6,6}};
        //Each sub-block
        for(int k=0;k<9;k++)
        {
            map<char, int>mp;
            for(int i=dir[k][0];i<dir[k][0]+3;i++)
            {
                for(int j=dir[k][1];j<dir[k][1]+3;j++)
                {
                    if(board[i][j]!='.'&&board[i][j]<'1'&&board[i][j]>'9') return false;
                    if(board[i][j]!='.')
                    {
                       mp[board[i][j]]++;
                       if(mp[board[i][j]]>1) return false;
                    }
                }
            }
        }
        return true;
    }
};


/*************************************************
39. Combination Sum
**************************************************/
/*Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
*/

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int> > res;
        vector<int> path;
        sort(candidates.begin(), candidates.end());
        dfs(res, path, candidates, 0, target);
        return res;

    }
    void dfs(vector<vector<int> > &res, vector<int> &path, vector<int>&nums, int start, int target)
    {
        if(target==0)
        {
           res.push_back(path);
           return;
        }
        if(target<0) return;
        for(int i=start;i<nums.size();i++)
        {
            path.push_back(nums[i]);
            dfs(res, path, nums, i, target-nums[i]);
            path.pop_back();
        }
    }
};

/*************************************************
40.Combination Sum II 
**************************************************/
/*Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
*/

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int> > res;
        vector<int> path;
        sort(candidates.begin(), candidates.end());
        dfs(res, path, candidates, 0, target);
        return res;

    }
    void dfs(vector<vector<int> > &res, vector<int> &path, vector<int>&nums, int start, int target)
    {
        if(target==0)
        {
           res.push_back(path);
           return;
        }
        if(target<0) return;
        for(int i=start;i<nums.size();i++)
        {
            if(i!=start&&nums[i]==nums[i-1]) continue;
            path.push_back(nums[i]);
            dfs(res, path, nums, i+1, target-nums[i]);
            path.pop_back();
        }
    }
};
============================
Hard:    037/041/042
============================

/*************************************************
37.  Sudoku Solver
**************************************************/
/*Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


A sudoku puzzle...


...and its solution numbers marked in red.
*/

class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        helper(board);
    }
    
    bool helper(vector<vector<char> > &board)
    {
        for(int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
                if(board[i][j] == '.')
                {
                    for(int k =1;k<=9;k++)
                    {
                        board[i][j] = k+'0';
                        if(isValid(board, i, j) && helper(board)) return true;
                        board[i][j] = '.';
                    }
                    return false;
                }
            }
        }
        return true;
    }
    
    bool isValid(vector<vector<char> > &board, int x, int y)
    {
        for(int i=0;i<9;i++)
        {
            if(i!=x && board[i][y] == board[x][y]) return false;
        }
        for(int j=0;j<9;j++)
        {
            if(j!=y && board[x][j] == board[x][y]) return false;
        }
        
        for(int i=3*(x/3);i<3*(x/3+1);i++)
        {
            for(int j=3*(y/3);j<3*(y/3+1);j++)
            {
                if(i!=x&&j!=y&&board[i][j] == board[x][y]) return false;
            }
        }
        return true;
    }
};

/*************************************************
41. First Missing Positive
**************************************************/
/*Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
*/

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
       int n=nums.size();
       for(int i=0;i<n;)
       {
           if(nums[i]!=i+1&&nums[i]>0&&nums[i]<=n&&nums[i]!=nums[nums[i]-1])
               swap(nums[i], nums[nums[i]-1]);
            else 
                i++;
       }
       for(int i=0;i<n;i++)
       {
           if(nums[i]!=i+1) return i+1;
       }
       return n+1;
        
    }
};

/*************************************************
42. Trapping Rain Water
**************************************************/
/*Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
*/

class Solution {
public:
    int trap(vector<int>& height) {
        if(height.size()<3) return 0;
        int n=height.size();
        vector<int> left_mx(n, 0);
        vector<int> right_mx(n,0);
        for(int i=0;i<n;i++)
            left_mx[i]=(i==0)?height[i]:max(left_mx[i-1], height[i]);
        for(int i=n-1;i>=0;i--)
            right_mx[i]=(i==n-1)?height[i]:max(right_mx[i+1], height[i]);
        int res=0;
        for(int i=0;i<n;i++)
        {
            res+=min(left_mx[i], right_mx[i])-height[i];
        }
        return res;
    }
};



