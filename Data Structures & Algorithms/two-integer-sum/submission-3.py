class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMatch = {} # val : index

        for i,n in enumerate(nums):
            diff = target - n 

            if diff in prevMatch:
                return [prevMatch[diff],i]
            prevMatch[n] = i
        return
