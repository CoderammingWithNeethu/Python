'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

class Solution:
    def twoSum_BruteForce(self, nums: list[int], target: int) -> list[int]:
        #Brute Force
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)): 
                if (nums[i]+nums[j]) == target:
                    return [i,j]

    #Optimizted Way
    def twoSum_Hashmap(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, value in enumerate(nums):
           remaining = target - nums[i]
           
           if remaining in seen:
               return [i, seen[remaining]]
            
           seen[value] = i 

           '''
           [7,2,13,11,8] ; target = 24
           {}<--- hashmap
           Required number = 24 - 7 = 17 is not present in our hashmap, so we add 7 as idxMap key and 0 as idxMap value 
           (0 is  the index of 7 in input array) {7:0}; repeat
           7- {7:0}
           2- {7:0,2:1}
           13- {7:0,2:1,13:2}
           Now required number = 24 - 11 = 13 is present in idxMap
           That means we have found the pair which adds up to the target sum 24, i.e. (11 , 13). 
           11- {7:0,2:1,13:2} ---> 13 req number is present in hashmap 
           '''

obj = Solution()
obj.twoSum([2,7,11,15],9) #[1, 2]
obj.twoSum([3,3],6) #[0, 1]
print(obj.twoSum([3,2,4],6))#[1, 2]