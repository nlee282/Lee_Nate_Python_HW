class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = []
        max = 0
        i = 0
        a = i
        while i < len(s):
            if arr.count(s[i]) > 0:
                arr = []
                i = s.find(s[i], a, len(s))+1
                a = i
            arr.append(s[i])
            if len(arr) > max:
                max = len(arr)
            i += 1
        return max
