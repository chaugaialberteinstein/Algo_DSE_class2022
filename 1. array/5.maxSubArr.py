class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr= max_ = nums[0]
        for i in nums[1:]:
            curr = max(i,curr+i)
            max_ = max(max_,curr )
        return max_
        
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         curr = nums[0]
#         max = curr
#         for i in range(len(nums)):
#             curr = max(nums[i], curr + nums[i])
#             max = max(max, curr)
#         return max
        