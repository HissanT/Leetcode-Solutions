This folder contains my solution to [LeetCode Problem 20: Valid Parentheses.](https://leetcode.com/problems/valid-parentheses/)

## **Problem Description**

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.  

A string is valid if:  
1. Open brackets are closed by the same type of brackets.  
2. Open brackets are closed in the correct order.  
3. Every close bracket has a corresponding previous open bracket.  

## **My Approach**

Not gonna lie — this one came out a bit messy. Instead of the usual clean stack solution, I built it a bit more *unconventionally*:  

1. **Dicts for open/close**  
   - Created two dictionaries to assign each type of bracket a numeric index.  

2. **Track with counter + stack**  
   - Pushed each opener with its index into a `latest` stack.  
   - Used `counter` to point at the “top” of the stack.  

3. **Match closers**  
   - On a closer, checked if it matched the top index.  
   - If yes → popped it.  
   - If no → returned `False`.  

4. **Handle edge cases**  
   - If the first char is a closer, caught that early.  
   - At the end, if anything was left on the stack → not valid.  

## **Notes**

- Initially, this didn’t work on **Python 2** (LeetCode default) because dict key ordering isn’t consistent there.  
- Switching to **Python 3** fixed it, since dicts now preserve insertion order.   

##

Not super proud of how it looks or performs — definitely not the simplest solution. But it felt good piecing it together in my own way. I’ll revisit this later to refactor for cleaner logic and better performance.  
