class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        words = []
        i=0
        for s in strs:
            s_dict = {}
            for char in s:
                if char not in s_dict:
                    s_dict[char]=1
                else:
                    s_dict[char]+=1
            if s_dict not in anagrams.values():
                anagrams[i] = s_dict
                words.append([s])
                i+=1
            else:
                for key in anagrams:
                    if anagrams[key] == s_dict:
                        words[key].append(s)
        return words