class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num = 0
        prefix = 1
        suffix = 1
        n = len(nums)
        output = [1] * n
    

        for i in range(n):
            output[i] *= prefix
            prefix *= nums[i]

        for i in range(n -1 , -1 , -1):
            output[i] *= suffix
            suffix *= nums[i]
        return output 