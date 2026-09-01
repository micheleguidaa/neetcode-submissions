class Solution:
    def isValid(self, s: str) -> bool:
        dict_par = {")":"(", "}":"{", "]":"["}
        stack = []

        for char in s:
            if char in dict_par.values():
                stack.append(char)
            elif stack and stack[-1] == dict_par[char]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
        

