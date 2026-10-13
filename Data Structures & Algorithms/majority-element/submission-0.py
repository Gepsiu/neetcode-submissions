class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)
        return max(hash_map, key=lambda x: hash_map[x])