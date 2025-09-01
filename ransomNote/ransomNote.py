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