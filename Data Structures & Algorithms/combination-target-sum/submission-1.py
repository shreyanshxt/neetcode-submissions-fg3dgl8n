class Solution:
    def combinationSum(self, nums: List[int], target: int):
        res=[]
        def dfs(start,target,path):
            if target==0:
                res.append(path[:])
                return 
            for i in range(start,len(nums)):
                if nums[i]>target:
                    continue
                dfs(i,target-nums[i],path+[nums[i]])
                
        dfs(0,target,[])
        return res
        
                

