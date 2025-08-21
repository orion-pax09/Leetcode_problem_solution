def search(nums,target):
    sort_num=sorted(nums)
    low=0
    high=len(sort_num)-1
    increment = 0
    while low <= high:
        sum = sort_num[low] + sort_num[high]
        if sum == target:
            increment +=1
            return f"The sum of value at index {low}+{high} gives {sum} from sorted array :- {sort_num} and it took {increment} attempts to find target "
        elif sum < target:
            increment +=1
            low +=1
        else:
            increment +=1
            high -=1
    return f"There is no target in this array"
Input = search([6,5,8,2,3,9,2,6],12)
print(Input)


