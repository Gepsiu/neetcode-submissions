class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        for char_s in s:
            hash_s[char_s] = 1 + hash_s.get(char_s, 0)
        for char_t in t:
            hash_t[char_t] = 1 + hash_t.get(char_t, 0)
        return hash_s == hash_t