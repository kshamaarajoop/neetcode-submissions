#brute force

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        n = len(prices)
        r = l+1
        prof = 0
        max = 0
        for i in range(n):
            p = i + 1
            for j in range(p,n):
                prof = prices[j] - prices[i]
                print(prices[j] - prices[i])
                
                if prof > max:
                    max = prof
        return max


            

        