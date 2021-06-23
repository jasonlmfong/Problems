from collections import Counter
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good = 0
        numsdict = Counter(nums)
        for i in numsdict:
            good += (numsdict[i]*(numsdict[i]-1))/2
        return good