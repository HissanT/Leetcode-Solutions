class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1
            else:
                k+=1
        nums.sort(reverse=True)
        return k