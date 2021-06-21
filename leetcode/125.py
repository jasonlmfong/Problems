class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = "".join(ch for ch in s if ch.isalnum())
        newstring = new.lower()
        left,right = 0, len(newstring)-1
        counter = 0
        while left < right:
            if newstring[left] != newstring[right]:
                return False
            left += 1
            right -= 1
        return True