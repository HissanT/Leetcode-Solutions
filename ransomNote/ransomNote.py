# Solution 1 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = {}

        for ch in magazine:
            if ch in hashMap:
                hashMap[ch] += 1
            else:
                hashMap[ch] = 1
        
        for ch in ransomNote:
            if ch in hashMap:
                if hashMap[ch] == 1:
                    del hashMap[ch]
                else:
                    hashMap[ch] -= 1
            else:
                return False
        return True

# Solution 2

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = Counter(magazine)

        for ch in ransomNote:
            if ch not in hashMap:
                return False
            if hashMap[ch] == 1:
                del hashMap[ch]
            else:
                hashMap[ch] -= 1

        return True
