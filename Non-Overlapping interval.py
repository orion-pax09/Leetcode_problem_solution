def non_overlapping_interval(intervals):
    if not intervals or len(intervals)==0:
        return f"There's no intervals"
    Interval=sorted(intervals, key=lambda x : x[1])
    i=0
    last_End=Interval[i][1]
    remove = 0
    n=len(Interval)
    for j in range(1, n):
        if Interval[j][0] >= last_End:
            i+=1
            last_End= Interval[j][1]
        else:
            remove +=1
    return remove
intervals = [[1,3],[2,4],[3,5],[5,6],[2,6]]
print(non_overlapping_interval(intervals))