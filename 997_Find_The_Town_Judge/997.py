class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        confianca = defaultdict(int)
        confiados = defaultdict(int)

        for x, y in trust:
            confiados[x] += 1
            confianca[y] =- 1

        for i in range(1, n + 1):
            if confianca.get(i, 0) == 0 and confiados.get(i, 0) == n - 1:
                return i 
        return -1