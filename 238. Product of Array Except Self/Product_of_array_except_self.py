# Approach:We are given an array nums and we have to find result array 
# where each element has product of all elements of nums array except 
# the element itself. Now we make a result array of same length 
# as nums array and initialize all elements with 1's. Let iterate over 
# range of length of nums array, now iterate the result array from forward 
# and backward simultaneously 

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
