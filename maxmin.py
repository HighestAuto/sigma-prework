def maxmin(arr_nums):
    maxmin = []
    temp = arr_nums[0]
    #checks the lowest munber
    for i in arr_nums:
        if i < temp:
            temp = i
    maxmin.append(temp)
    for i in arr_nums:
        if i > temp:
            temp = i
    maxmin.append(temp)
    return maxmin

print(maxmin([100,-100]))