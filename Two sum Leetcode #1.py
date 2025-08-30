#TIme complexity: O(n²)
def Two_sum(nums,targets):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == targets:
                return i,j
    
    return f"None"
Input=Two_sum([3,6,2,5,7,9,10],8)
print(Input)


#Time complexity: O(n)
def two_sum(num,target):
    seen={}
    for i , num in enumerate(num):
        complement= target -  num
        if complement in seen:
            return (seen[complement],i)      
    seen[num]=i
nput=two_sum([3,6,2,5,7,9,10],8)
print(nput)