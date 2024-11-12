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
