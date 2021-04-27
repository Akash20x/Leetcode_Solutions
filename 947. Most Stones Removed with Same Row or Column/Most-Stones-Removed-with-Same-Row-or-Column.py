# Approach:We are given a 2D array showing coordinates of stones in a 2D plane.
# We have to remove stones from 2D plane if it shares row or column with any other stone,
# and we have to find largest possible number of stones that can be removed with above condition.
# To solve this, we have to create a dictionary and iterate over location of each stone and calculate 
# union find(a) of each stone with row or column (to check stone can be removed with this 
# row or column or not) and store it as a key value pair for each stone.
# Here union find used for 2 things: 
# a) To determine which group a particular element belongs to.
# b) Find no of groups that has no effect on each other if element of one group is changed or removed.
# Now we take union find of all elements of dictionary to calculate union find(b) groups.
# Now to find largest no of stones that can be removed=Total no of stones - union find(b) groups.
# Theoritically, No of union find groups = No of stones that cannot be removed as either it has 
# following conditions :
# A) It will be last element left to be removed
# B) It may not be the last element but it belongs to different group which neither share row 
# or column with their group elements.

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = {}
        def find(x):
            if x != uf.setdefault(x, x):
                uf[x] = find(uf[x])
            return uf[x]
        for i, j in stones:
            uf[find(i)] = find(~j)
        return len(stones) - len({find(x) for x in uf})  
