class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        qr = []
        for q, w in zip(quality, wage):
            qr.append([w / q, q])
        qr.sort()
		
		#Find the first valid total wage, having first K workers with lowest w/q rate. 
        cand, csum = [], 0
        for i in range(K):
            heapq.heappush(cand, -qr[i][1]) #min heap 
            csum += qr[i][1]
        ans = csum * qr[K - 1][0]  #The first answer is the K-th LOWESET w/q rate, times the total quality of these workers.

		#Each time we push the idx-th quality in heap, and get the first K-th LOWEST w/q rate by popping out the largest one from heap, then multiple the total sum by idx-th rate.
        for idx in range(K, len(quality)):
            heapq.heappush(cand, -qr[idx][1])
            csum += qr[idx][1] + heapq.heappop(cand)
            ans = min(ans, csum * qr[idx][0])
        return ans
        
