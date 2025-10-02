# my solutsion:

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange-1
            emptyBottles += 1
            numExchange += 1
        return emptyBottles


sol = Solution()
print(sol.maxBottlesDrunk(13, 6))
