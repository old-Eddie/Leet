class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = "1"
        while True:
            if int(ans, 2) >= n:
                return int(ans, 2)
            else:
                ans += "1"
                print(ans)


sol = Solution().smallestNumber
print(sol(3))
