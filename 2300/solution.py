from typing import List
from functools import cache

# my solution


class Solution:
    @cache
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
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
    def valid_pos(self, potions: List[int], success: int, spell: int) -> int:
        potion_needed = (success + spell - 1) // spell
        l, r = 0, len(potions)
        while l < r:
            mid = l + (r - l) // 2
            if potions[mid] >= potion_needed:
                r = mid
            else:
                l = mid + 1
        return l

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for spell in spells:
            res.append(len(potions) - self.valid_pos(potions, success, spell))
        return res
