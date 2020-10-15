class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lenght = len(nums)
        for i in range(lenght):
            i = abs(nums[i]) - 1
            if nums[i] > 0: nums[i] = -nums[i]
        return [i + 1 for i in range(lenght) if nums[i] > 0]