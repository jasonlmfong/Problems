class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        banks = len(accounts[0])
        cust = {}
        for customer_id in range(len(accounts)):
            cust[customer_id] = sum(accounts[customer_id])
        return max(cust.values())