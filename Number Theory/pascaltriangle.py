class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        res = [[0],[1],[1,1]]
        if n <= 2:
