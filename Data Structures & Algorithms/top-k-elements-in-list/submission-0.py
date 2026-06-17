class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_common = {}
        freq = [[]for i in range(len(nums) + 1)]
        res = []
        # Add 5 students with scores
        for i in nums:
            most_common[i] = 1 + most_common.get(i,0)
        for i , c in most_common.items():
            freq[c].append(i)
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res