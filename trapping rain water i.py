def trapping_Water(array):
    size= len(array)
    left_wall=[0]*size
    right_Wall=[0]*size
    max_left=0
    total_Water=0
    for i in range(size):
        max_left=max(max_left,array[i])
        left_wall[i]=max_left
    max_right=0
    for i in reversed(range(size)):
        max_right = max(max_right,array[i])
        right_Wall[i]=max_right
    for i in range(size):
        trapped= min(left_wall[i],right_Wall[i]) - array[i]
        if trapped > 0 :
            total_Water +=trapped
    return total_Water
INPUT=trapping_Water([3,1,2,4,0,1,3,2])
print(INPUT)


