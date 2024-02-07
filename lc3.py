def lengthOfLongestSubstring(s: str) -> int:
    temp_letters = {}
    ans = ''
    temp_ans = ''
    i = 0
    while i < len(s):
        if s[i] in temp_letters:
            if len(temp_ans) > len(ans):
                ans = temp_ans
            temp_ans = ''
            i = temp_letters.get(s[i])
            temp_letters = {}
        else:
            temp_letters[s[i]] = i
            temp_ans += s[i]
        i += 1
    if len(temp_ans) > len(ans):
        ans = temp_ans
    return len(ans)

print(lengthOfLongestSubstring('dvdf'))