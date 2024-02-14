def findMin(nums) -> int:
    start = 0
    end = len(nums)-1
    if nums[start] < nums[end]:
        return nums[start]
    else:
        while nums[start] > nums[end]:
            mid = (start + end)//2
            if mid==start:
                break
            if nums[mid] > nums[start]:
                start = mid+1
            elif nums[mid] < nums[end]:
                if nums[mid-1] < nums[mid]:
                    end = mid - 1
                else:
                    end = mid
                    break
    return min(nums[start], nums[end])

print(findMin([2, 1]))
            