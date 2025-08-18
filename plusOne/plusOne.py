class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for d in digits:
            s += str(d)
        s = str(int(s) + 1)
        return [int(c) for c in s]
    
    
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits