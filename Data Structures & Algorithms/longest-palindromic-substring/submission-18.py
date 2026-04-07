class Solution:
    def is_pali(self, s):
        left, right = 0, len(s)-1
        while left<=right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s[0]
        longest = ""
        for i in range(len(s)):
            for j in range(len(s), i-1, -1):
                substring = s[i:j]
                
                if self.is_pali(substring):
                    if len(substring) > len(longest):
                        longest = substring
                    break
        return longest

        