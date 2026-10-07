class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            for idx in range(i + 1, len(nums)):
                if nums[i] == nums[idx]:
                    res.append(1)
        return len(res)