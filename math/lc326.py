def isPowerOfThree(n: int) -> bool:
    if n <= 0:
        return False
    def recursor(n, curr):
        if curr==n:
            return True
        if n >= 1 and curr > n:
            return False
        if n < 1 and curr < n:
            return False
        if n >= 1:
            return recursor(n, curr*3)
        else:
            return recursor(n, curr/3)
    return recursor(n, 1)

print(isPowerOfThree(0))