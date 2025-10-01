class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = numBottles
        while numBottles >= numExchange:
            emptyBottles += 1
            numBottles -= numExchange-1
        return emptyBottles


sol = Solution()
print(sol.numWaterBottles(9,3))
