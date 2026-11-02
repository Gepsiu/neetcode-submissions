class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        idx = 0

        if len(word1) <= len(word2):
            l = len(word1)
            word = word2
        else:
            l = len(word2)
            word = word1
        while idx < l:
            result += word1[idx]
            result += word2[idx]
            idx += 1
        if len(word) > idx:
            return result + word[idx:]
        return result
