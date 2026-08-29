class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diz = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in diz:
                return [diz[diff], i]
            if num not in diz:
                diz[num] = i
