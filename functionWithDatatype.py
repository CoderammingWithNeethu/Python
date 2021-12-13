from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            if i < len(nums)-1:
                if sum([nums[i],nums[i+1]]) == target:
                    return [i,i+1]

x = Solution()
print(x.twoSum([3,2,4],6))   