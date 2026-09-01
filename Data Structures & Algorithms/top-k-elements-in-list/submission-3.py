from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        
        reversed_counter = defaultdict(list)
        for key , value in counter.items():
            reversed_counter[value].append(key)

        output = []
        for i in range(len(nums), 0, -1):
            for num in reversed_counter[i]:
                 output.append(num)
                 if len(output) == k:
                    return output
