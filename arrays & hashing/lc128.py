# https://leetcode.com/problems/longest-consecutive-sequence/description/

def longestConsecutive(nums):
    if len(nums)==0: return 0
    ans = 1
    temp = 1
    nums = sorted(nums)
    nums = list(dict.fromkeys(nums))
    print(nums)
    for i in range(len(nums)-1):
        if nums[i]+1 == nums[i+1]:
            temp += 1
        else:
            if temp >= ans:
                ans = temp
            temp = 1
    if temp >= ans:
        ans = temp
    return ans

