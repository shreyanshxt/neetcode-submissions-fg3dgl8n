class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        num=[]
        res=[]
        def dfs(i):
            if i>=len(nums):
                res.append(num.copy())
                return
            
            num.append(nums[i])
            dfs(i+1)
            num.pop()
            dfs(i+1)
        dfs(0)
        print(res)
        return res