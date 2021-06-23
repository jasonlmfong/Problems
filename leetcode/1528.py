class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        letters = {}
        result = ""
        for j in range(len(s)):
            letters[indices[j]] = s[j]
        for i in range(len(s)):
            result += letters[i]
        return(result)