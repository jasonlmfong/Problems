class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum =0
        sums =[]
        for i in nums: 
            sum +=i
            sums.append(sum)
        return sums