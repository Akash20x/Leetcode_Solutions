# Approach: There are total n coins and we have to find
# K coins which completely filled k staircase rows but
# didn't exceed total coins.No of coins that can be completely
# filled in k rows is k(k+1)/2 which must be less than
# or equal to n,this form a quadratic equation and on solving value 
# of K,we get required answer.


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)



