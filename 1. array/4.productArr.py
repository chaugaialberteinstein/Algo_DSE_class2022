class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            prefix = 1
            suffix = 1
            n = len(nums)
            l_arr=[0]*n
            r_arr=[0]*n
            for i in range(n):
                j= -i-1
                l_arr[i] = prefix
                r_arr[j] = suffix
                prefix *= nums[i]
                suffix *= nums[j] 
            return [p*s for p,s in zip(l_arr,r_arr)]
