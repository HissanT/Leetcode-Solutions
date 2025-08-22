This folder contains my solution to [LeetCode Problem 58: Length of Last Word.](https://leetcode.com/problems/length-of-last-word/)  

## **Problem Description**

Given a string `s` consisting of words and spaces, return the length of the **last word** in the string.  
A word is defined as a maximal substring consisting of non-space characters only.  

## **My Approach**

Honestly, this one was pretty straightforward—almost felt like a warm-up problem:  

1. **Trim spaces**  
   - Used `.strip()` to get rid of trailing and leading spaces so I don’t have to deal with messy edge cases.  

2. **Count backwards**  
   - Started from the end of the string and kept counting characters until I hit a space.  

3. **Return count**  
   - As soon as a space is found (or we hit the start), just return the count.  

##  

Got this one really early, maybe even on my first submission. 
Super simple, but still satisfying to solve cleanly.  
