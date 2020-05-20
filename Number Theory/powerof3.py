class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        from math import floor,ceil,sqrt
        x = log10(n)/log10(3)
        
