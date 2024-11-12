class Solution(object):
    def dfs(self, cursos, visitado, no):
            visitado[no] = False
            for vizinho in cursos[no]:
                if self.dfs(cursos, visitado, vizinho) == False:
                    return False
            visitado[no] = True
            return True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCursos: int
        :type preRequisitos: List[List[int]]
        :rtype: bool
        """
        cursos = {i: [] for i in range(numCourses)}
        for x, y in prerequisites:
            cursos[x].append(y)
        visitado = [None] * numCourses
        for i in range(numCourses):
            if not self.dfs(cursos, visitado, i):
                return False
        return True