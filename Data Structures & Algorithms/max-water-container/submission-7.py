class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            j = i+1
            if j<len(heights):
                 while i<j and j<len(heights):
                    calc=min(heights[j],heights[i])*int(j-i)
                    if area<calc:
                        area = calc
                        
                    j += 1
        
            else:
                break
        return area
            
           
        