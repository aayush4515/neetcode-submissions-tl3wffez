class Solution:

    # def encode(self, strs: List[str]) -> str:
    #     encoded_str = ""
    #     for s in strs:
    #         len_str = len(s)
    #         encoded_str += str(len_str) + '#' + s
    #     print(encoded_str)
    #     return encoded_str
        

    # def decode(self, s: str) -> List[str]:
    #     decoded_list = []

    #     i = 0
    #     while i < len(s):
    #         curr_str = ""
    #         j = i
    #         while s[j] != '#':
    #             j +=1
            
    #         len_str = int(s[i:j])
    #         curr_str = s[j + 1 : len_str + j + 1]
    #         decoded_list.append(curr_str)

    #         i = len_str + j + 1
            
    #     return decoded_list

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            len_s = len(s)
            res += str(len_s) + "#" + s
        
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            len_str = int(s[i : j])
            res.append(s[j + 1 : j + len_str + 1])

            i = j + len_str + 1
        
        return res
    




















