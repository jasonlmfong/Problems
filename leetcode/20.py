class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {")":"(", "}":"{", "]":"["}
        stack = []
        for item in s:
            if item in dict:
                if not stack:
                    return False
                if dict[item] != stack.pop():
                    return False
            else:
                stack.append(item)
        return stack == []