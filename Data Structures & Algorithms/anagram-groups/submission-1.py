class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''comDic = {}
        for item in strs:
            count = [0] * 26
            for c in item:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in comDic:
                comDic[tuple(count)].append(item)
            else:
                comDic[tuple(count)] = [item]
        res = list(comDic.values())
        return res'''

        # using defaultdict
        comDic = defaultdict(list)
        for item in strs:
            count = [0] * 26
            for i in item:
                count[ord(i) - ord('a')] += 1
            comDic[tuple(count)].append(item)

        return list(comDic.values())

