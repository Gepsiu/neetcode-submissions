class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}

        bucket = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)

        for val, c in count_map.items():
            bucket[c].append(val)
        
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res