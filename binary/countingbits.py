class Solution:
    def countBits(self, num: int) -> List[int]:
        bits=[0]*(num+1)
        for i in range(num+1):
            bits[i]=bits[i//2]+i%2
        return bits