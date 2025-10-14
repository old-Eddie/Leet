from math import floor
from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        def mono(idx: int) -> bool:

            for i in range(idx, idx + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False

            return True

        for idx in range(len(nums) - k - k + 1):
            if mono(idx) and mono(idx + k):
                return True

        return False


sol = Solution().hasIncreasingSubarrays
print(sol([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], k=5))
