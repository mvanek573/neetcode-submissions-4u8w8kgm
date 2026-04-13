class Solution:
    def encode(self, strs):
        new_str = ""
        i = 0
        while i < len(strs):
            if len(strs[i])==0:
                new_str+=chr(17)
            else:
                j=0
                while j<len(strs[i]):
                    new_str+=chr(ord(strs[i][j])+1 % 256)
                    j+=1
            if i != len(strs)-1:
                new_str+=' '
            i+=1
        return new_str
            
    def decode(self, s):
        new_str = []
        i = 0
        flag = True
        while i < len(s):
            if ord(s[i])==17:
                new_str.append("")
            elif s[i]==' ':
                flag = True
            else:
                if flag:
                    new_str.append("")
                    flag = False
                new_str[-1] += chr(ord(s[i])-1 % 256)
            i+=1
        return new_str
