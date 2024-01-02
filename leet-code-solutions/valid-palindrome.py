class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        output = ""
        s = s.lower()
        for char in s:
            if char.isalnum():
                output += char

        return output == output[::-1]