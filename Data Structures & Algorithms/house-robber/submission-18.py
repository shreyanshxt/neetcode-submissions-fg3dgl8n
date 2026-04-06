class Solution:
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for i  in nums:
            temp = now
            now = max(last + i, now)
            last = temp
            print("last",last,"temp",temp,"now",now)
        return now