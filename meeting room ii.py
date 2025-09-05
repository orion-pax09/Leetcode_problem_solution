import heapq
def NMEETINGROOMii(interval):
    Interval=sorted(interval,key=lambda x: x[0])
    heap=[]
    heapq.heappush(heap,Interval[0][1])
    for s in range(1,len(interval)):
        start,end=Interval[s]
        if start >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap,end)
    return len(heap)
nput=NMEETINGROOMii([[2,3],[4,6],[7,9],[2,5],[3,6],[5,9],[4,7]])
print(nput)
    



