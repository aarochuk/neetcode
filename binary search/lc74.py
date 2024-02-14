"""def searchMatrix(matrix, target):
    for i in range(len(matrix)):
        if matrix[i][len(matrix[i])-1] < target:
            continue
        elif matrix[i][0] > target:
            break
        else:
            low = 0
            high = len(matrix[i])
            while low <= high:
                mid = (low+high)//2
                if matrix[i][mid] > target:
                    high = mid-1
                elif matrix[i][mid] < target:
                    low = mid + 1
                elif matrix[i][mid] == target:
                    return True
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))"""

def searchMatrix(matrix, target):
    maLow = 0
    maHigh = len(matrix)-1
    prevI = -1
    while maLow < maHigh:
        i = (maHigh + maLow)//2
        if i == prevI:
            break
        else:
            prevI = i
        if matrix[i][len(matrix[i])-1] < target:
            maLow = i+1
        elif matrix[i][0] > target:
            maHigh = i-1
        else:
            low = 0
            high = len(matrix[i])
            while low < high:
                mid = (low+high)//2
                if matrix[i][mid] > target:
                    high = mid-1
                elif matrix[i][mid] < target:
                    low = mid + 1
                elif matrix[i][mid] == target:
                    return True
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))