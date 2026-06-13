class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums :
            if x in seen:
                pass
            seen.add(x)
        uni_ele = set(nums)
        if len(uni_ele) < len(nums):
            return True
        else:
            return False