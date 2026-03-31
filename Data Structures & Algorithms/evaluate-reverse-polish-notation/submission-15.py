class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i].isnumeric() or tokens[i].lstrip('-').isdigit():
                stack.append(tokens[i])
                print(stack,"1")
            elif tokens[i]=="+":
                sum=int(stack[-2])+int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(sum)
                print(stack,"2")
            elif tokens[i]=="*":
                prod=int(stack[-1])*int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(prod)
                
                print(stack,"3")
            elif tokens[i]=="-":
                sub=int(stack[-2])-int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(sub)
            else :
                div=int(stack[-2])/int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(div)
                print(stack,"5")
        print(stack)
        return int(stack[-1])