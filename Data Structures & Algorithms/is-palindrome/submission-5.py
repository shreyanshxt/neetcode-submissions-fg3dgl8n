class Solution:
    def isPalindrome(self,s: str) -> bool:
        s=s.lower()
        for i in s:
            if i.isalnum() == False:
                s=s.replace(i,"")
      
        print(s)
        
        print(s)
        s=s.replace("?","")
        pal=list(s)
        
        pal.reverse()
        print("pak",pal)
        lap=list(s)
        print("lap",lap)
        
        if pal == lap :
            return True
        else :
            return False