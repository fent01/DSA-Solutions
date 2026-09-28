class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        table = {}
        for i,num in enumerate(nums):
            needed = target-num

            if needed in table:
                return[table[needed], i]

            table[num] = i
        
