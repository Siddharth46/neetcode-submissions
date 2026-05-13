'''class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        while len(strs) > 0:
            curr = strs[0]
            A = [0]*26
            temp = []
            i = 1
            while i < len(strs):
                if len(curr) != len(strs[i]):
                    i += 1
                    continue
                for j in range(len(curr)):
                    A[ord(curr[j]) - ord('a')] += 1
                    A[ord(strs[i][j])-ord('a')] -= 1
                is_ana = True
                for val in A:
                    if val != 0:
                        is_ana = False
                if is_ana:                        
                    temp.append(strs.pop(i))
                else:
                    i += 1
                    break
            temp.append(strs.pop(0))
            res.append(temp)
        return res'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        comDic = {}
        for item in strs:
            count = [0] * 26
            for c in item:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in comDic:
                comDic[tuple(count)].append(item)
            else:
                comDic[tuple(count)] = [item]
        res = list(comDic.values())
        return res

