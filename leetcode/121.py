class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        currentmaxprofit = 0
        if len(prices) <= 1:
            return currentmaxprofit
        low = prices[0]
        previousday = prices[0]
        for day in prices[1:]:
            if day < previousday:
                low = min(low, day)
            else:
                currentmaxprofit = max(currentmaxprofit, day - low)
            previousday = day
        return currentmaxprofit