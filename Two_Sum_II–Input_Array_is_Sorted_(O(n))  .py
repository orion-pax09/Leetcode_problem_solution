def search(array):
    head,tail=0,len(array)-1
    result = [0] * len(array)
    pros= len(array)-1
    while head <= tail:
        if abs(array[tail]) > abs(array[head]):
            result[pros] = array[tail] ** 2
            tail -=1
        else:
            result[pros] =  array [head] ** 2
            head +=1
        pros -=1
    return sorted(result)






input=search([3,4,1,2])
print(input)

