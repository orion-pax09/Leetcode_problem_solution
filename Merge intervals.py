def mergeinterval(s):
    if not s or s==0:
        return None
    intervals=sorted(s)
    i=0
    n=len(intervals)
    for j in range(1,n):
        if intervals[i][1]>=intervals[j][0]:
            intervals[i][1]=max(intervals[i][1],intervals[j][1])
        else:
            i +=1
            intervals[i]=intervals[j]
    return f"{intervals[:i +1]}"



Input=mergeinterval([[3,4],[1,5],[6,3],[5,8],[2,7],[15,70],[5,18]])
print(Input)