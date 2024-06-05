class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        
        return list( (i + extraCandies) >= m for i in candies)
