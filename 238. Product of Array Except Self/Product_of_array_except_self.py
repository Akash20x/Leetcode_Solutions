# Approach:We are given an array nums and we have to find result array 
# where each element has product of all elements of nums array except 
# the element itself. Now we make a result array of same length 
# as nums array and initialize all elements with 1's. Let iterate over 
# range of length of nums array, now iterate the result array from forward 
# and backward simultaneously multiplied by value of p and q respectively
# with respective elements to find the final result array. Initial value of p
# and q is 1,and to find all other values, we have to iterate nums array both
# forward and backward simultaneously with consecutive multiplication of their
# elements from both sides and store it in p and q respectively till the loop ends.
# The final result array we get when all iterations over is the required answer. 

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
