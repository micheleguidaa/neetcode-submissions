class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = dict()
        counter2 = dict()

        for char in s:
            counter1[char] = counter1.get(char, 0) + 1

        for char in t:
            counter2[char] = counter2.get(char, 0) + 1
        
        return counter1 == counter2
