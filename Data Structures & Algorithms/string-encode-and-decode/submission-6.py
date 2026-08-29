class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded
        

    def decode(self, s: str) -> List[str]:
        i = 0
        number_string = ""
        decoded_list = []
        while i < len(s):
            if ord('0') <= ord(s[i]) <= ord('9'):   
                number_string += s[i]          
                i += 1
            if s[i] == "#":
                len_string = int(number_string)
                number_string = ""
                stringa = str(s[ i + 1: i + 1 + len_string])
                decoded_list.append(stringa)
                i = i + 1 + len_string
        return decoded_list
            

