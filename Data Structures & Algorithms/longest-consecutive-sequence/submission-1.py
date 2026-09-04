class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        current_len = 0
        max_len = current_len
        for num in nums:
            if num - 1 in set_nums:
                continue
            else:
                current_len = 1
                i = 1
                while num + i in set_nums:
                    current_len += 1
                    i += 1
                max_len = max(current_len, max_len)
        return max_len


        