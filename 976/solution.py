from typing import List


class Solution:
# Mine:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = []
        max = 0
        for i in range(len(nums)-2):
            if (nums[i] + nums[i+1] > nums[i+2]):
                ans.append(i)
            else:
                None
        if len(ans) > 0:
            for i in ans:
                if nums[i]+nums[i+1]+nums[i+2] > max:
                    max = nums[i]+nums[i+1]+nums[i+2]
        return max
# Best:
        # nums.sort(reverse=True)
        # for i in range(len(nums) - 2):
        #     if nums[i + 1] + nums[i + 2] > nums[i]:
        #         return nums[i] + nums[i + 1] + nums[i + 2]
        # return 0


solution = Solution()
ans = solution.largestPerimeter(nums=[3, 2, 3, 4])
print(ans)
