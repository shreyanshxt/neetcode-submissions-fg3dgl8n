class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        for i in range(0,len(nums)):
            max=nums[i]
            for j in range(i,len(nums)):
                if nums[j]<nums[i]:
                    max=nums[i]
                    nums[i]=nums[j]
                    nums[j]=max
                    j+=1
               
                

