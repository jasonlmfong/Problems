class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numsdict={}
        for index, number in enumerate(sorted(nums)):
            if number not in numsdict:
                numsdict[number] = index
        return [numsdict[n] for n in nums]