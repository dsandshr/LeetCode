# input: [1,2,3,4,5,2,3,1] -> output: 5
# input: [4,1,2,1,2] -> Output: 4
# Input: [1]-> Output: 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if nums:
            for i in nums:
                if nums.count(i) == 1:
                    return i
        return None