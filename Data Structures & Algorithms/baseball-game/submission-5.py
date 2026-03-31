class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in range(len(operations)):
            if operations[i].isnumeric() or operations[i].lstrip('-').isdigit() :
                stack.append(operations[i])
                print("for adding",stack)
            elif operations[i]=="+":
                print(operations[i-1])
                print(operations[i-2])
                summ=int(stack[-1]) + int(stack[-2])
                print(summ)
                stack.append(summ)

            elif operations[i]=="C":
                stack.pop()
            elif operations[i]=="D":
                print("this",stack)
                score=2*int(stack[-1])
                score_f=str(score)
                stack.append(score_f)
                print(stack)
        print(stack)
        sum=0
        for i in range(len(stack)):
            sum=sum+int(stack[i])
        return sum

        

                