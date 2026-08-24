class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            piles.sort()
            k = piles[-1]
            return k
        k = i/hr