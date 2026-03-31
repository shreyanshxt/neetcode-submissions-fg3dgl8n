class Solution:
    def rotate(self,nums: List[int], k: int) -> None:
        k = k % len(nums)
        rotm=[0]*k
        for i  in range(k):
    
            rotm[i]=nums[(len(nums)-k)+i]
        rotm.extend(nums[0:len(nums)-k])
        nums[:] = rotm