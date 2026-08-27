from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            group_anagrams[sorted_word].append(word)
        return list(group_anagrams.values())