class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [hash_map[diff], i]
            if num not in hash_map:
                hash_map[num] = i
