from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)
        for char in set(counter_s.keys()) | set(counter_t.keys()):
            if counter_s[char] != counter_t[char]:
                return False
        return True
