This folder contains my solution to [LeetCode Problem 383: Ransom Note](https://leetcode.com/problems/ransom-note/).

## **Problem Description**

Given two strings `ransomNote` and `magazine`, the task is to determine if `ransomNote` can be constructed from the letters in `magazine`.

* Each letter in `magazine` can only be used once.
* Return `True` if construction is possible, otherwise `False`.

---

## **My Approach**

I implemented **two different solutions**, both based on tracking character frequencies:

### **Solution 1 – Manual HashMap**

1. Loop through `magazine` and build a frequency dictionary manually.
2. For every character in `ransomNote`:

   * If it exists in the dictionary, decrement its count (or delete if count becomes zero).
   * If it does not exist, return `False`.
3. If all characters pass the check, return `True`.

---

### **Solution 2 – Using `Counter()`**

* Instead of writing the first loop manually, I used `collections.Counter(magazine)` to directly build the frequency dictionary.
* The rest of the logic remains identical—check each character in `ransomNote`, decrement, or delete.

This shows how the **entire first loop in Solution 1** is elegantly replaced with a single `Counter()` call.

---

## **Complexity Analysis**

* **Time Complexity:** `O(n + m)` where `n = len(ransomNote)`, `m = len(magazine)`
* **Space Complexity:** `O(m)` for the frequency map

---

Pretty straightforward problem once you see the frequency map approach. The `Counter()` version is much cleaner and more Pythonic while keeping the same logic.
