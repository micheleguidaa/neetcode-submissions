from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        counter1 = Counter(s1)
        left = 0
        right = len(s1)
        counter2 = Counter(s2[left:right])
        if counter1 == counter2:
            return True
        while right < len(s2):
            counter2[s2[left]] -= 1
            counter2[s2[right]] += 1
            if counter1 == counter2:
                return True
            left += 1
            right += 1

        return False



        