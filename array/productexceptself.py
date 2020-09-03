class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro=1
        arr=[]
        l=len(nums)
        for i in range(l):
            arr.append(pro)
            pro*=nums[i]
        pro=1
        for i in range(l-1,-1,-1):
            arr[i]*=pro
            pro*=nums[i]
        return arr