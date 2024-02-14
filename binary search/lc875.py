def minEatingSpeed(piles, h):
    start = 1
    end = max(piles)
    while start < end:
        mid = (start+end)//2
        if start==mid:
            break
        for i in piles:
            if i % mid > 0:
                curr += 1
            curr += i//mid
        if curr <= h:
            end = mid
        else:
            start = mid
    return end
print(minEatingSpeed(piles = [30,11,23,4,20], h = 6))