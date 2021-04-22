# Approach:We are given n workers with their wage and quality respectively, and we have to find
# k workers where each worker have their wages in ratio with quality and they should be paid 
# minimum wage exceptation as mention in wages. Let take an array with wage/quality ratio and 
# respective quality and sort the array for n workers in accordance with wage/quality ratio. 
# Now we take a loop to iterate over first k group of workers and push first k group of 
# workers quality with negative sign in the minimum heap (first element every time 
# smallest,rest elements push and pop) and find total quality.Now calculate for first k group 
# of workers total wages = max(wage/quality) ratio * total quality (sum of quality of first
# k workers).Here we consider maximum wage /quality ratio so that every worker should get their
# minimum wage as we consider highest wage amount. Now iterate over next k group of workers and 
# so on till we reach all quality values and push their quality values in heap and delete the 
# quality value of first K-1 workers from heap to calculate the quality value of ongoing k workers 
# and multiplied it with maximum wage/quality ratio (total quality= max(wage/quality) ratio * total quality).
# Now consider the minimum total wages out of two total wages we calculate to find least 
# amount of money needed to form a paid group satisfying the above conditions.

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        qr = []
        for q, w in zip(quality, wage):
            qr.append([w / q, q])
        qr.sort()
		
        cand, csum = [], 0
        for i in range(K):
            heapq.heappush(cand, -qr[i][1]) #min heap 
            csum += qr[i][1]
        ans = csum * qr[K - 1][0] 

        for idx in range(K, len(quality)):
            heapq.heappush(cand, -qr[idx][1])
            csum += qr[idx][1] + heapq.heappop(cand)
            ans = min(ans, csum * qr[idx][0])
        return ans
        
