class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(start,target,path):
            if target==0:
                res.append(path[:])
                return res
            for i in range(start,len(nums)):
                if start<i and nums[i]==nums[i-1]:
                    continue
                if nums[i]>target:
                    break
                dfs(i+1,target-nums[i],path+[nums[i]])
        
        nums.sort()
        dfs(0,target,[])
        return res



        

    