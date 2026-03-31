class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged=[]
        merged.extend(nums2)
        merged.extend(nums1[:m])
        print(merged)
        merged.sort()
        for i in range(len(merged)):
            nums1[i]=merged[i]
            
