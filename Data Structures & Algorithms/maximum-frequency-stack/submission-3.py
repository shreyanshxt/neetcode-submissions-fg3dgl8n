from collections import Counter

class FreqStack:

    def __init__(self):
        self.dic=defaultdict(int)
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.dic[val]+=1


    def pop(self) -> int:
        max_cc=max(self.dic.values())
        i=len(self.stack)-1
        while self.dic[self.stack[i]] != max_cc:
            i -=1
        self.dic[self.stack[i]] -=1
        return self.stack.pop(i)
        