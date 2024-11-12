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

        for src, dst in trust:
            confiados[dst] = confiados.get(dst, 0) + 1  # Incrementa o número de pessoas que confiam em 'dst'
            confianca[src] = confianca.get(src, 0) - 1  # Decrementa a confiança de 'src'

        for i in range(1, n + 1):
            if confianca.get(i, 0) == 0 and confiados.get(i, 0) == n - 1:
                return i  # Se 'i' não confia em ninguém (confianca[i] == 0) e todos confiam nele (confiados[i] == n-1), é o juiz
        return -1