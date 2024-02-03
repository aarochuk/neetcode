def threeSum(nums):
    solu = []
    nums = nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        first = i
        start = i+1
        end = len(nums)-1
        while start < end:
            if nums[start]+nums[end] < -nums[first]:
                start += 1
            elif nums[start]+nums[end] > -nums[first]:
                end -= 1
            else:
                solu.append([nums[first], nums[start], nums[end]])
                end -= 1

                while nums[end] == nums[end-1]:
                    end -= 1
    return solu

print(threeSum([-2,0,1,1,2]))