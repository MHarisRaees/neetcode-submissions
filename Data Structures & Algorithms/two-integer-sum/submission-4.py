class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMatch = {} # val : index

        for i,n in enumerate(nums): # i for index , n for value
            diff = target - n #find difference

            if diff in prevMatch: # check elements in PrevMatch
                return [prevMatch[diff],i] # return indexes
            prevMatch[n] = i # continue
        return
