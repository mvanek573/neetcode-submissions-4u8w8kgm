import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            products.append(math.prod(nums[1::]))
            temp = nums[0]
            nums.pop(0)
            nums.append(temp)
        return products