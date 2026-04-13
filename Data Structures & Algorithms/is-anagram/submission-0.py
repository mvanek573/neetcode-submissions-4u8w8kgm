class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = {}
        for char in s:
            if char not in letters:
                letters[char]=1
            else:
                letters[char]+=1
        for char in t:
            if char not in letters:
                return False
            else:
                letters[char]-=1
                if letters[char] == 0:
                    letters.pop(char)
        if len(letters) != 0:
            return False
        return True
        