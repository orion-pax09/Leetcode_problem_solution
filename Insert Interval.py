def insert_intervals(intervals,new_interval):
    interval=sorted(intervals, key=lambda x:x[0])
    result=[]
    i=0
    n=len(interval)

    while i < n and interval[i][1] < new_interval[0]:
        result.append(interval[i])
        i +=1

    while i < n and  interval[i][0] <= new_interval[1]:
        new_interval[1]=max(interval[i][1],new_interval[1])
        new_interval[0]=min(interval[i][0],new_interval[0])
        i +=1
    result.append(new_interval)

    while i < n:
        result.append(interval[i])
        i+=1

    return result


print(insert_intervals([[1,3],[6,9]], [2,5]))
