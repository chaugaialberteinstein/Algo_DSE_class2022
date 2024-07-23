# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dic={}
        for i in nums:
            if i in dic:
                return True
            else:
                dic[i]=-19
        return False
