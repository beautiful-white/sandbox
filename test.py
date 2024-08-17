from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp: List[int] = [1] + [0] * (amount + max(coins) + 1)
        for coin in coins:
            for i in range(amount):
                dp[i + coin] += dp[i]
        return dp[amount]


def main() -> None:
    s = Solution()
    print(s.change(amount=5, coins=[1, 2, 5]))

if __name__ == "__main__":
    main()