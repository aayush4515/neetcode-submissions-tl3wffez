class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            len_str = len(s)
            encoded_str += str(len_str) + '#' + s
        print(encoded_str)
        return encoded_str
        

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        # for i in range(0, len(s) - 1):
        #     curr_str = ""
        #     if s[i].isdigit() and s[i + 1] == '#':
        #         len_str = s[i]
        #         curr_str = s[i+2 : i + int(len_str) + 2]
        #         decoded_list.append(curr_str)

        i = 0
        while i < len(s):
            curr_str = ""
            if s[i].isdigit() == False:
                i += 1
                continue
            j = i
            while s[j] != '#':
                j +=1
            
            len_str = int(s[i:j])
            curr_str = s[j + 1 : len_str + j + 1]
            decoded_list.append(curr_str)

            i = len_str + j + 1
            
        return decoded_list