class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        l = 0
        r = len(palindrome) - 1
        palindrome = list(palindrome)

        while l < r:
            if palindrome[l] != "a":
                palindrome[l] = 'a'
                return "".join(palindrome)
            l += 1
            r -= 1
        if len(palindrome) > 1 and len(set(palindrome)) == 1:
            palindrome[-1] = "b"
            return "".join(palindrome)
        elif len(palindrome) != 1 and l == r:
            palindrome[-1] = 'b'
            return "".join(palindrome)
        
        return ""