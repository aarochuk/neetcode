# https://leetcode.com/problems/group-anagrams/description/

def groupAnagrams(strs):
    output = []
    group = {}
    i = 0
    for str in strs:
        s = ''.join(sorted(str))
        if s in group:
            output[group[s]].append(str)
        else:
            group[s] = i
            output.append([str])
            i+=1
    return output
