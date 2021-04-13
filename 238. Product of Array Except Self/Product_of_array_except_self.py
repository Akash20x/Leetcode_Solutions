class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p,q=1,1
        results=[1]*len(nums)
        for i in range(len(nums)):
            results[i]*=p
            results[~i]*=q
            p*=nums[i]
            q*=nums[~i]
        return results
