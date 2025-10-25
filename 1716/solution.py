class Solution(object):
    def totalMoney(self, n):

        total = (((n // 7) * ((n // 7) - 1)) // 2) * 7
        total += (n // 7) * 28
        total += (((n % 7) * ((n % 7) + 1)) // 2) + ((n // 7) * (n % 7))

        return total
