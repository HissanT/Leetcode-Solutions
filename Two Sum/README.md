This folder contains my solution to [LeetCode Problem 1: Two Sum.](https://leetcode.com/problems/two-sum/)

## **Problem Description**

Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.  
The answer can be returned in any order.

---

## My Approach  

At first, the brute force approach looked tempting (double for-loops and check every pair).  
It works, but is inefficient with a time complexity of **O(n²)**.  

After digging a little deeper, I learned the more **clever & efficient way** using a **hashmap**:  

1. **Iterate with index and value**  
   - For each `num` in `nums`, calculate the difference `diff = target - num`.  

2. **Check the hashmap**  
   - If `diff` already exists in the hashmap, we’ve found the solution.  
   - Return the indices: `[hashMap[diff], i]`.  

3. **Otherwise, add the number to hashmap**  
   - Store the current `num` as the key and its index `i` as the value.  

This reduces the complexity to **O(n)**, which feels like magic compared to brute force.  

---

Honestly, it gives me a chuckle how one problem can be solved in such **different yet clever ways**, from brute force chaos to clean hashmaps.  
