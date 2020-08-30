class Solution:
    def hammingWeight(self, n: int) -> int:
        ones=0
        while n:
            if n%2==1:
                ones+=1
            n//=2
        return ones
        