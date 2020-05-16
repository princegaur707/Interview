# https://leetcode.com/problems/maximum-product-subarray/submissions/
class Solution:
    def maxProduct(self,A: List[int]) -> int:
        B = A[::-1]
        for i in range(1,len(A)):
            if A[i-1] != 0:
                A[i]*=A[i-1]
