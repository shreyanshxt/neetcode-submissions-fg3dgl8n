class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in range(len(operations)):
            if operations[i].isnumeric() or operations[i].lstrip('-').isdigit() :
                stack.append(operations[i])
            elif operations[i]=="+":
                summ=int(stack[-1]) + int(stack[-2])
                stack.append(summ)
            elif operations[i]=="C":
                stack.pop()
            elif operations[i]=="D":
                score=2*int(stack[-1])
                score_f=str(score)
                stack.append(score_f)
        sum=0
        for i in range(len(stack)):
            sum=sum+int(stack[i])
        return sum

        

                