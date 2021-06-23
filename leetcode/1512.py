class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsdict = {}
        good = 0
        for i in nums:
            if i in numsdict:
                numsdict[i] += 1
            else:
                numsdict[i] = 1
            good += (numsdict[i] - 1)
        return good