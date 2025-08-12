import statistics


def median_of_three(num):
    array=num
    selection1=sorted(array[:3])
    selection2=sorted(array[3:])
    def finding_median(medians):
        medians.extend(selection1 + selection2)
        calculating_median=statistics.median(medians)
        if calculating_median:
            medians.clear()
            return calculating_median
    result=finding_median([])
    return result
number=median_of_three([3,4,6,2,8,9])
print(number)


