class Solution:
    def groupAnagrams(self, strs):
        if len(strs) < 2:
            return str
        result = {}
        for s in strs:
            tmp = tuple(sorted(s))
            result[tmp] = result.get(tmp, []) + [s]
        return list(result.values())
