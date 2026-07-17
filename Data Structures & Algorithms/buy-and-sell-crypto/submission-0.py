class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      ## we will define i as the day that we buy the the stock and j the day at which we can sell the stock
      # Iterate through the array prices to count all possibles options

        lowest = prices[0]
        best = 0

        for price in prices:
            if price < lowest:
                lowest = price
            best = max(best, price - lowest)

        return best