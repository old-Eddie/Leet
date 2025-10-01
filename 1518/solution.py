# my solutsion:

"""
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = numBottles
        while numBottles >= numExchange:
            emptyBottles += 1
            numBottles -= numExchange-1
        return emptyBottles
"""
# best solution:
"""
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles-1)//(numExchange-1)
"""
