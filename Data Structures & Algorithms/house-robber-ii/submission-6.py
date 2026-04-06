class Solution:
    def rob(self, nums: List[int]) -> int:
        window=len(nums)-1
        print(window)
       
        new_l=list(nums)
        lis=[]
        nums.extend(new_l)
        print(nums)
        if window==0:
            return nums[0]
        else:
            for i in range(int(len(nums)/2)):
            
                ele=nums[i:window+i]
                print("ele",ele)
                last, now = 0, 0
                for n  in ele:
                    temp = now
                    now = max(last + n, now)
                    last = temp
                lis.append(now)
                print("lis",lis)
            return max(lis)
            
        


