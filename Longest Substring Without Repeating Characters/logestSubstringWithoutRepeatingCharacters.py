class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenSet = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in seenSet:
                seenSet.remove(s[left])
                left += 1
            seenSet.add(s[right])
            longest = max(longest, right - left + 1)
        return longest