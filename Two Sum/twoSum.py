class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # add num : index pair AFTER checking if it's difference is in the hashmap
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[num] = i