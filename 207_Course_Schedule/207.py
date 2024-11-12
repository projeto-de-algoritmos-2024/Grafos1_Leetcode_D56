class Solution(object):
    def dfs(self, cursos, visitado, no): # Busca em profundidade
            if visitado[no] is False: # Se o nó ainda não foi visitado, retorna falso
                return False
            if visitado[no] is True: # Se o nó já foi visitado, retorna verdadeiro
                return True
            visitado[no] = False
            for vizinho in cursos[no]: # Para cada vizinho do nó
                if self.dfs(cursos, visitado, vizinho) == False:
                    return False
            visitado[no] = True
            return True

    def canFinish(self, numCourses, prerequisites):
        
        cursos = {i: [] for i in range(numCourses)}
        for x, y in prerequisites:
            cursos[x].append(y)
        visitado = [None] * numCourses # Inicializa a lista de visitados vazia
        for i in range(numCourses):
            if not self.dfs(cursos, visitado, i):
                return False
        return True