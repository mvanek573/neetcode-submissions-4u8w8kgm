class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True
        # unique = set()
        # for num in nums:
        #     if num not in unique:
        #         unique.add(num)
        #     else:
        #         return True
        # return False