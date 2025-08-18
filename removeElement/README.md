This folder contains my solution to [LeetCode Problem 27: Remove Element.](https://leetcode.com/problems/remove-element/)
## **Problem Description**

Given an integer array nums and an integer val, the task is to remove all occurrences of val in-place and return the new length k of the array.

The relative order of the elements may be changed, but the first k elements should hold the final result.
## My Approach  

Instead of shifting elements or using the classic two-pointer method, I did something a bit different and it turned out 🔥:  

1. **Mark unwanted values**  
   - Whenever `nums[i] == val`, replace it with `-1` (dummy placeholder).  

2. **Count valid elements**  
   - Increment `k` every time `nums[i] != val`.  

3. **Sort with `reverse=True`**  
   - Sort the list in descending order so that all `-1`s drop to the back automatically.  
   - The first `k` elements are then the valid result.
  
##

Got to use `reverse=True` in `sort()`, which not everyone thinks about using in problems like this.
Ended up cleaner than expected, and surprisingly dominated performance stats.
