class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        res = [[0],[1],[1,1]]
        if n <= 2:
            return res[1:n+1]
        for i in range(3,n+1):
            newrow = [0]*(i)
            newrow[0] = newrow[-1] = 1
            for j in range(1,len(newrow)-1):
                newrow[j] = res[-1][j]+res[-1][j-1]
            res.append(newrow)
    
        return res[1:]
