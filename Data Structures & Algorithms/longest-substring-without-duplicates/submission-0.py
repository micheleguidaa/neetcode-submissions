class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = left
        seen_chars = set()

        current_len = 0
        max_len = current_len
        while right < len(s):
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1
                current_len -= 1 
            seen_chars.add(s[right])
            current_len += 1
            if current_len > max_len:
                max_len = current_len
            right += 1
        return max_len
        
        