from collections import Counter

class FreqStack:

    def __init__(self):
        self.Stack = []
        self.Stack2 = []

    def push(self, val: int) -> None:
        self.Stack.append(val)

    def pop(self) -> int:
        if not self.Stack:
            return None  

        count = Counter(self.Stack)
        max_freq = max(count.values())

        
        most_common_all = [item for item, c in count.items() if c == max_freq]
        print ("most",most_common_all)
        
        while self.Stack:
            top = self.Stack.pop()
            print("stack1",self.Stack)
            if top in most_common_all:
                
                while self.Stack2:
                    print("stck2",self.Stack2)
                    self.Stack.append(self.Stack2.pop())
                return top
            else:
                self.Stack2.append(top)

        return None  # fallback (should not hit)