from typing import List

# my ans


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        temp = []
        while len(nums) != 1:
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1] >= 10:
                    nums[i] = nums[i]+nums[i+1]-10
                else:
                    nums[i] = nums[i]+nums[i+1]
            nums.pop()
        return int(nums[0])

# best ans
# class Solution:
#     def triangularSum(self, nums: List[int]) -> int:
#         n=len(nums)-1
#         ans, A=nums[0], 1
#         for k in range(1, n+1):
#             A=A*(n-k+1)//k
#             ans=(ans+nums[k]*A)%10
#         return ans
