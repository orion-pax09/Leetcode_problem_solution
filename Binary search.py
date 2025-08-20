def search(numbers,target):
    left=0
    right = len(numbers)-1
    while left <= right:
        middle= (left+right) // 2
        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            left= middle +1
        else:
           right = middle - 1
    return "There is no target in this array"
INPUT=search(sorted([6,9,8,3,19,4,80,92,800,55]),80)
print(INPUT)



