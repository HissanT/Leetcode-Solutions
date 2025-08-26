This folder contains my solution to [LeetCode Problem 3: Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## **Problem Description**

Given a string `s`, return the length of the **longest substring** without repeating characters.

A **substring** is a contiguous sequence of characters within a string.

---

## **My Approach**

This one introduced a **new concept for me from Blind 75** — the **sliding window** — and it was confusing at first. I’m definitely going to revisit it a few times to let it fully click. Hard one, but super satisfying once it works!

I used a **two-pointer sliding window** with a **hash set** to track the current window’s characters:

1. **Window & Set**

   * Maintain a window `[left, right]` and a `seenSet` containing the characters currently in the window.

2. **Expand with `right`**

   * Iterate `right` across the string.
   * If `s[right]` is **not** in `seenSet`, it’s safe to expand the window:

     * Add `s[right]` to the set.
     * Update `longest = max(longest, right - left + 1)`.

3. **Shrink with `left`**

   * If `s[right]` **is** already in the set (duplicate!), shrink the window from the left:

     * Repeatedly remove `s[left]` from the set and increment `left` until the duplicate is gone.
   * Then add `s[right]` and keep going.

This guarantees the window always contains **unique** characters.

---

## **Why It Works**

* The window only moves **forward** (each character enters and leaves at most once), so the total work is linear.
* The set keeps membership checks **O(1)** on average, letting us quickly decide whether to expand or shrink.

---

## **Complexity**

* **Time:** `O(n)` — each char is added/removed from the set at most once.
* **Space:** `O(k)` — where `k` is the size of the character set in the current window (at most min(`n`, alphabet size)).

---

## **Notes & Pitfalls I Hit**

* Don’t try to “restart” the window on duplicates — **shrink from the left** until the duplicate is removed.
* Be careful to **update `longest` after adding `s[right]`** and ensuring the window is valid.
* Edge cases:

  * Empty string `""` → `0`
  * All same chars `"aaaa"` → `1`
  * All unique `"abcde"` → `len(s)`

---

Got to learn sliding windows properly here — tough at first, but it’s a pattern that shows up **everywhere**. I’ll be revisiting this one a few times to lock it in.
