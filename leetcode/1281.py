class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        Prod = 1
        Sum = 0
        for i in str(n):
            Prod *= int(i)
            Sum += int(i)
        return Prod - Sum