class Solution:
    def validPalindrome(self, s: str) -> bool:
        s=s.lower()
        for i in s:
            if i.isalnum() == False:
                s=s.replace(i,"")
        s=s.replace(" ","")
        
        def is_palindrome(string):
            return string == string[::-1]

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Try deleting character at left or right index
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
            left += 1
            right -= 1
        
        return True