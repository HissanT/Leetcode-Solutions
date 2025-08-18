This folder contains my solution to [LeetCode Problem 66: Plus One](https://leetcode.com/problems/plus-one/)

# LeetCode Problem 66: Plus One  

## **Problem Description**  
You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `i`th digit of the integer.  
The digits are ordered from most significant to least significant in left-to-right order.  

The task: **Increment the large integer by one and return the resulting array of digits.**

---

## **My Approaches**  

### **1. Python’s Magic Shortcut (felt like cheating)**  
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for d in digits:
            s += str(d)
        s = str(int(s) + 1)
        return [int(c) for c in s]
```

- Converted the list into a string → turned it into an integer → added one → converted it back.

- Felt too easy though, like Python did the job for me with its built-in shenanigans.

- Works perfectly, but almost feels like I didn’t actually solve the problem myself.

### 2. The “Real” Way (Manual Digit Handling)
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits
```

- Start from the rightmost digit.

- If it’s a 9, turn it into 0 and carry over.

- If it’s not 9, just add 1 and stop.

- If everything rolls over (like 999 → 1000), just add a 1 at the front.
