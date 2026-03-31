class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water=[0]
        for i in range(len(heights)):
            for j in range(len(heights)):
                dist=abs(i-j)
                if heights[i]<heights[j]:
                    max_val=dist*heights[i]
                    water.append(max_val)
                    

                else:
                  max_val=dist*heights[j]
                  water.append(max_val)

        return max(water)