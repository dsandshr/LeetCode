# The "Majority" element is the element that appears more than [n / 2] times.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = dict()
        for i in nums:
            if i in dic: dic[i] += 1
            else: dic[i] = 1
        for i, x in dic.items():
            if x > len(nums) / 2:
                return i