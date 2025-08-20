This folder contains my solution to [LeetCode Problem 121: Best Time to Buy and Sell Stock.](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)  

## **Problem Description**  

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.  

The task is to find the **maximum profit** you can achieve from a single buy-and-sell transaction. If no profit is possible, return `0`.  

---

## **My Approach**  

This one felt **relatively easy** compared to other array problems, but still neat to work through:  

1. **Track the minimum price**  
   - Start with the first element as the "buy" price.  

2. **Update as you go**  
   - As we iterate through prices, if we find a lower price, we update our "buy".  

3. **Calculate potential profit**  
   - At each step, check if selling at the current price gives a better profit than what we have so far.  

4. **Return the max profit**  
   - At the end, `res` holds the best trade we could’ve made.  

---

## **Why this worked well**  
- Only **one pass** through the array → `O(n)` time.  
- Constant extra space → `O(1)` space.  

---

Honestly, this problem was more about careful **tracking** than brute force. One of those "don’t overthink it" problems. Pretty clean and efficient solution.  
