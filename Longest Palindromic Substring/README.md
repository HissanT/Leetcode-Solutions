
This folder contains my solution to **[LeetCode Problem 5: Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)**.

## **Problem Description**

Given a string `s`, return the **longest palindromic substring** in `s`.
A palindrome reads the same forward and backward (e.g., `aba`, `abba`).

---

## **My Approach**

This one was the **hardest** I’ve done so far—lots of tricky, confusing ideas at first. I finally wrapped my head around it and got it working. The core idea is **expand-around-center**:

1. **Track best answer**

   * Keep `res` (best substring) and `maxLen` (its length).

2. **Expand for every center**

   * For each index `i`, expand outward while characters match.
   * Do it **twice** per `i`:

     * **Odd-length** center at `(i, i)` → catches palindromes like `aba`.
     * **Even-length** center at `(i, i+1)` → catches palindromes like `abba`.

3. **Update when we find a longer palindrome**

   * If current window `s[left:right+1]` beats `maxLen`, update `res` and `maxLen`.

> **Why both odd & even every time?**
> Because the string as a whole being odd/even length doesn’t tell you anything about the **palindrome’s** length at a specific center. A string like `"babad"` (odd length) still contains even-length palindromes in general, and vice versa. Checking **both** per index guarantees we don’t miss any.


---

## **Complexity**

* **Time:** `O(n^2)` in the worst case (each index can expand across the string).
* **Space:** `O(1)` extra space (ignoring the output substring).

---

## **Edge Cases Considered**

* Single-character strings (`"a"`) → return the char itself.
* All identical characters (`"aaaaa"`) → returns the entire string.
* No repeating chars (`"abc"`) → any single char is a palindrome.
* Mixed centers where the longest palindrome sits between characters (even-length).

---

## **Mini Dry Run**

`s = "babad"`

* Center at `i=0` (`"b"`): longest around here → `"bab"`
* Center at `i=1` (`"a"`): expands to `"aba"` (same length)
* Final answer could be `"bab"` or `"aba"` (both correct)

---

## **What I Learned / Reflection**

This was **very hard** for me initially. The part that tripped me up was **checking both odd and even palindromes at every index**—it felt counterintuitive because I kept thinking about the **whole string’s** length instead of the **local palindrome’s** length.
I’ve now understood the intuition and flow, but I’ll **revisit** this to make sure I retain it.

---

## **Alternatives I Might Explore Later**

* **DP (Dynamic Programming):** `O(n^2)` time and `O(n^2)` space; builds a table of palindromic substrings.
* **Manacher’s Algorithm:** `O(n)` time, more complex but fastest.

---

## **Notes**

* Expanding from the center is clean, easy to code, and passes comfortably.
* Remember: **always** run **both** expansions at each index.
