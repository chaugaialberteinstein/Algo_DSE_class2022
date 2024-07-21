class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]  # Initialize minimum price
        profit = 0

        for current_price in prices[1:]:  # Iterate through prices from index 1
            # Update minimum price if current price is lower
            min_price = min(min_price, current_price)
            # Calculate and update profit if current price - min_price is higher
            profit = max(profit, current_price - min_price)

        return profit
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         minPrice = prices[0]
#         profit = 0
#         for i in prices[1:]:
#             current_price = prices[i]
#             buy_price = current_price - minPrice
            
#             if profit > buy_price:
#                  profit = buy_price

#         return profit
       