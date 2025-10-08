from typing import List
from functools import cache

# my solution


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        @cache
        def multpliyer(i, j):
            return i*j
        ans = [0]*len(spells)
        for i in range(len(spells)):
            for j in range(len(potions)):
                if multpliyer(spells[i], potions[j]) >= success:
                    ans[i] += 1
        return ans

# best solution:


class Solution:
    def successfulPairs(self, spells, potions, success):
        sorted_potions = sorted(potions)
        result = []
        for a in spells:
            count = len(sorted_potions) - \
                bisect_left(sorted_potions, (success + a - 1) // a)
            result.append(count)
        return result
