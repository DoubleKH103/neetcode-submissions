class Solution:
    def maxArea(self, heights: List[int]) -> int:
        k = 0
        j = len(heights) - 1 
        max = 0
        for i in range(len(heights)):
            while k < j:
                current = (j - k) * min(heights[j], heights[k])
                if current >= max :
                    max = current
                    if heights[j] < heights[k]:
                        j -= 1
                    elif heights[j] > heights[k]:
                        k += 1
                    else :
                        j -= 1
                        k += 1
                else :
                    if heights[j] < heights[k]:
                        j -= 1
                    elif heights[j] > heights[k]:
                        k += 1
                    else:
                        j -= 1
                        k += 1

        return max