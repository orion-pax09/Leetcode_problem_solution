import heapq


def trappingwater(heightmap):
    if not heightmap or  not heightmap[0]:
        return 0
    m,n=len(heightmap), len(heightmap[0])
    visited=[[False]*n for _ in range(m)]
    heap=[]
    for i in range(m):
        for j in range(n):
            if i ==0 or i == m-1 or j == 0 or j == n-1:
                heapq.heappush(heap,(heightmap[i][j],i,j))
                visited[i][j]=True

    water_Trapped=0
    max_Water=0
    direction= ([1,0],[-1,0],[0,1],[0,-1])
    while heap:
        height, x,y=heapq.heappop(heap)
        max_Water=max(max_Water,height)
        for dx,dy in direction:
            nx,ny =  x+dx, y+dy
            if 0 <= nx < m and 0 <=ny < n and not visited[nx][ny]:
                visited[nx][ny]=True
                if heightmap[nx][ny] < max_Water:
                    water_Trapped += max_Water - heightmap[nx][ny]
                    heapq.heappush(heap,(heightmap[nx][ny],nx,ny))
    return water_Trapped
INPUT=trappingwater([[1,4,3,1,3,2],
                     [3,2,1,3,2,4],
                     [2,3,3,2,3,1]])
print(INPUT)