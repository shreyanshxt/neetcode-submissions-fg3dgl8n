class Solution:
    def numRescueBoats( self,people: List[int], limit: int) -> int:
        length=len(people)
        people.sort()
        print(people)
        i=0
        j=length-1
        boats=[]
        while i<j:
            if people[i]+people[j] == limit :
                list1=[people[i],people[j]]
                boats.append(list1)
                i=i+1
                j=j-1

            elif people[i]+people[j] >limit:
                list1=[people[j]]
                boats.append(list1)
                j=j-1
            else:
                list1=[people[i],people[j]]
                boats.append(list1)
                i=i+1
                j=j-1
        if i==j:
            list1=[people[i]]
            boats.append(list1)
       

        print(boats)
        return len(boats)


