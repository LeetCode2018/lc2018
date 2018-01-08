"""
34. Search for a Range
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution:
    def searchLeft(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return left
    
    def searchRight(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return right
        
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = self.searchLeft(nums, target), self.searchRight(nums, target)
        #print(left, right)
        if left >= len(nums) or right >= len(nums) or nums[left] != target or nums[right] != target:
            return [-1, -1]
        else:
            return [left, right]

"""
36. Valid Sudoku
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
"""
class Solution:
    def isValid(self, valueList):
        res = [i for i in valueList if i != '.']
        return len(res) == len(set(res))

    def isValidRow(self, board):
        for row in board:
            if not self.isValid(row):
                return False
        return True
    
    def isValidCol(self, board):
        for col in zip(*board):#TODO: means zip(board[0], board[1], ..., board[len(board)])
            if not self.isValid(col):
                return False
        return True

    def isValidSquare(self, board):
        for row in (0,3,6):
            for col in (0,3,6):
                square = [board[i][j] for i in range(row, row+3)
                                        for j in range(col, col+3)]
                if not self.isValid(square):
                    return False
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.isValidRow(board) and self.isValidCol(board) and self.isValidSquare(board)

"""
39. Combination Sum
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

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
"""
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if len(candidates) == 0:
            return []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if nums[i] > target:  
                break
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)

"""
40. Combination Sum II
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

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
"""
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if len(candidates) == 0:
            return []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        res = sorted(res)
        return [res[i] for i in range(len(res)) if i == 0 or res[i]!=res[i-1]]

    def dfs(self, nums, target, index, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if nums[i] > target:  
                break
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], res)

"""
53. Maximum Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = curr = nums[0]
        for num in nums[1:]:
            curr = max(curr+num, num)
            maxnum = max(curr, maxnum)
                
        return maxnum

"""
58. Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        length, res, metchar = len(s), 0, False
        for c in s[::-1]:
            print(c)
            if c != ' ': res += 1; metchar = True
            elif metchar: break
            else: continue
        return res