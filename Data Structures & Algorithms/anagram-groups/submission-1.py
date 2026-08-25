class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anagrams = dict()
        for word in strs:
            key = "".join(sorted(word))
            dict_anagrams[key] = dict_anagrams.get(key, []) + [word]
        return list(dict_anagrams.values())