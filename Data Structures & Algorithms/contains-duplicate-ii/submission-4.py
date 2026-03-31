class Solution:
    def containsNearbyDuplicate( self,nums: List[int], k: int) -> bool:
        l=len(nums)
        for i in range(l):
            for j in range(i + 1,l):
                if nums[i]==nums[j] and abs(i-j)<=k:
                    return True
    
        return False