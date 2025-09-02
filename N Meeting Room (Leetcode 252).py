def NMeetingroom(interval):
    Intervals=sorted(interval, key=lambda  x: x[0])
    n= len(Intervals)
    for i in range(0, n-1):
        if Intervals[i][1]>Intervals[i+1][0]:
            return False
    return True
nput = NMeetingroom([[3,5],[5,8],[2,3]])
g=NMeetingroom([[2,4],[4,6],[2,6]])
print(g)
print(nput)