def median_Sorted_array(array1,array2):
    total=len(array1) + len(array2)
    if total % 2 == 1:
        half=(total + 1) // 2
    else:
        half = total //2
        #ensure array1 is smaller array
    if len(array1) > len(array2):
        array1,array2 = array2,array1
    else:
        low,high=0,len(array1)
        while low <= high:
            partition_X=(low + high) //2
            partition_Y=half - partition_X
            # if array1 has no element on left side

            if partition_X ==0:
                maxleft_X=float("-inf")
            else:
                maxleft_X = array1[partition_X-1]
            #if array1 has no element on right side

            if partition_X == len(array1):
                minright_X=float("inf")
            else:
                minright_X=array1[partition_X]

            #if array2 has no element on left side

            if partition_Y == 0:
                maxleft_Y = float("-inf")
            else:
                maxleft_Y=array2[partition_Y-1]

            #if array2 has no element on right side

            if partition_Y == len(array2):
                minright_Y=float("inf")
            else:
                minright_Y=array2[partition_Y]

                #ensure that left side of middle element should be less than right side of middle elements

            if maxleft_X <= minright_Y and maxleft_Y <= minright_X:
                if total % 2==1:
                    return max(maxleft_X,maxleft_Y)
                else:
                    return  (max(maxleft_X,maxleft_Y)+min(minright_Y,minright_X)) / 2

            #if left side of middle element is greater ot equal to right side of middle elements
            elif maxleft_X > minright_Y:
                high = partition_X - 1
            else:
                low = partition_X + 1



INPUT=median_Sorted_array(sorted([3,4,6,7]),sorted([4,6,9,1,10]))
print(INPUT)