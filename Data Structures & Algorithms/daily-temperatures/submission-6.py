class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack=[]
        count=[0]*len(temp)
        for i in range(len(temp)):
            stack.append(temp[i])
            
            
            for j in range(i+1,len(temp)):
                stack.append(temp[j])
               
                if temp[j]>stack[0]:
                    count[i]=len(stack)-1

                
                    break
                
            stack.clear()
        print(count)
        return count

              

                
               
        
            

            
           
           
           
           
           