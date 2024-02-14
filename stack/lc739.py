def dailyTemperatures(temperatures):
    ans = [0 for i in temperatures]
    stack = []
    for i in range(len(temperatures)):
        if i == 0:
            stack.append(i)
        else:
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                ans[stack[-1]] = i  - stack[-1]
                stack.pop()
            stack.append(i)
    return ans
print(dailyTemperatures(temperatures = [30,30,30]))
