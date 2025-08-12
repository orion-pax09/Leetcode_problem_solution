import statistics

def x(nums):
    array=nums
    total_sum=0
    sorting=sorted(array, reverse=True) #sort the array in descending number
    while len(sorting) >=3:
        selection_three=sorting[:3] #selection of largest value in first three elements in sorted array
        finding_median=statistics.median(selection_three)  #finding median among first 3 elements
        total_sum += finding_median #to find how much did it take to add with median of each three element in each steps
        del sorting[:3] # to remove first three elements after finding median and adding it to toal value
    return total_sum
y=x([5,4,3,2,6,7,5,4,6,7,9,34,5,6,7,5,555,6,7,8,3])
print(y)








