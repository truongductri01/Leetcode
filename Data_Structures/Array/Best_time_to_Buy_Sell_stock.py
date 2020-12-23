'''
    Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
'''


class Solution:
    def maxProfit(self, prices: list) -> int:
        '''
            Vars:
                1. temp - temporary buy values
                2. profit - the profit

            Process:
                Loop through the prices array
                If any price that could create a higher profit,
                    then profit = price - temp
                Else if the price is lower than the temp's value
                    => temp is assigned with the value of price

            Time Complexity: O(n) as only loop through the array once
        '''
        if len(prices) <= 1:
            return 0
        else:
            temp = prices[0]
            profit = 0  # 0
            for price in prices:
                if price - temp > profit:
                    # only updates when you can have more profit
                    # update the profit
                    profit = price - temp
                    # print("Buy at {}, sell at {}, profit: {}".format(buy, sell, profit))
                elif price < temp:
                    temp = price
                    # print("Updating temp at: {}".format(temp))
            return profit
