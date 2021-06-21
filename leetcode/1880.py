class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        firstValue = ""
        for i in range(len(firstWord)):
            firstValue += str(ord(firstWord[i])-97)
            
        secondValue = ""
        for i in range(len(secondWord)):
            secondValue += str(ord(secondWord[i])-97)
        
        targetValue = ""
        for i in range(len(targetWord)):
            targetValue += str(ord(targetWord[i])-97)
            
        return int(firstValue)+int(secondValue) == int(targetValue)