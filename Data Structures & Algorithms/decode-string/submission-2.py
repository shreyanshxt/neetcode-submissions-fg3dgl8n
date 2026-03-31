class Solution:
    def decodeString(self, s: str) -> str:
        char=[]
        for i in range(len(s)):
            if s[i]!=']':
                char.append(s[i])
            else:
                sub=""
                while char[-1]!='[':
                    sub=char.pop()+sub
                char.pop()
                k=""
                while char and char[-1].isdigit():
                    k=char.pop()+k
                char.append(sub * int(k))
        print("char",char)
        return "".join(char)
        
        
