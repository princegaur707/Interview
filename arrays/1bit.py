https://leetcode.com/problems/number-of-1-bits/
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         return bin(n).count('1')

class Solution:
    def countBits(self, num: int) -> List[int]:
        bits=[0]*(num+1)
        for i in range(num+1):
            bits[i]=bits[i//2]+i%2
        return bits

Solution sol 
n=input("Enter: ")
print(sol.countBits(n))