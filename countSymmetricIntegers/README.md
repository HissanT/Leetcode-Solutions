This folder contains my solution to [LeetCode Problem 2843: Count Symmetric Integers.](https://leetcode.com/problems/count-symmetric-integers/)  

## **Problem Description**

You are given two positive integers `low` and `high`.  
A **symmetric integer** is defined as an integer with an even number of digits such that the sum of the first half of its digits equals the sum of the second half.  

Return the number of symmetric integers in the inclusive range `[low, high]`.

---

## **My Approach**

Honestly, this one was a bit tricky, but not the hardest — especially considering I haven’t really studied much for LeetCode so far. Still, it pushed me to think about string manipulation and digit handling:  

1. **Iterate through range**  
   - For every integer between `low` and `high`, convert it into a string so I can easily split digits.  

2. **Check even length only**  
   - If the number has an odd digit length, skip it (because symmetric integers are only defined for even digit counts).  

3. **Split into halves**  
   - Divide the string into two equal halves.  
   - Store digits of first half in `arrF`, and second half in `arrE`.  

4. **Sum digits & compare**  
   - Compute the sum of digits in both halves.  
   - If the sums match, it’s symmetric → increment counter `c`.  

5. **Return result**  
   - At the end, return the total count of symmetric integers.  

---

## **Notes**
- I found this problem fun since it relied more on string slicing and digit sums rather than pure math formulas.  
- The solution is straightforward but requires careful handling of halves and sums.  
- Could probably be optimized, but clarity > micro-optimization at this stage.  

---
