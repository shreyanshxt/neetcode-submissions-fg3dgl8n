class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def back(start,target,path):
            if target==0:
                res.append(path[:])
                return
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                if nums[i]>target:
                    break
                back(i+1,target-nums[i],path+[nums[i]])
        nums.sort()
        back(0,target,[])
        return res
        

    