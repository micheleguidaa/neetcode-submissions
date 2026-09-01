class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        profit = 0
        max_proft = profit

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit >= max_proft:
                max_proft = profit
                right += 1
            else:
                if profit >= 0:
                    right += 1
                else:
                    left = right
                    right += 1
        return max_proft


        