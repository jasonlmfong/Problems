class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max = -float("inf")
        currMax = -float("inf")
        
        for num in nums:
            currMax = max(num, num + currMax)
            Max = max(Max, currMax)
        return Max