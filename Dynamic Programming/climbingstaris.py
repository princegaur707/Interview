# https://leetcode.com/problems/climbing-stairs/
class Solution:
    stairs = [0,1,2]
    def climbStairs(self, n: int) -> int:
        try:
            return self.stairs[n]
        except:
            for i in range(len(self.stairs),n+1):
                self.stairs.append(self.stairs[-1]+self.stairs[-2])
            return self.stairs[n]
        
