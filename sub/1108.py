class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        newadd=""
        for i in range(len(address)):
            if address[i] == ".":
                newadd += "[.]"
            else:
                newadd += address[i]
        return newadd