
from collections import Counter
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for x in nums:
            y = target - x
            if y in nums and x!=y:
                return [nums.index(x), nums.index(y)]
            elif y in nums and x==y:
                if Counter(nums)[x]>1:
                    return [nums.index(x), nums.index(x,1)]







