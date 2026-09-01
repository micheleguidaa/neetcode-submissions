class Solution:
    def encode(self, strs: List[str]) -> str:
        enconding = ""
        for word in strs:
            enconding += str(len(word)) + "#" + word
        return enconding

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        string_len = ""
        i = 0
        while  i < len(s):
            while s[i].isdigit():
                string_len += s[i]
                i += 1
            if s[i] == "#":
                len_word = int(string_len)
                string_len = ""
                stringa = s[ i + 1 : i + len_word + 1]
                decoded_list.append(stringa)
                i = i + len_word + 1
        return decoded_list
            


