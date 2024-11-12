# Find if Path Exists in Graph

**Problema disponível no LeetCode:** [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)

## Descrição

Dado um grafo não-direcionado com \( n \) nós numerados de \( 0 \) a \( n - 1 \) e uma lista de arestas, determine se existe um caminho entre dois nós específicos, `source` e `destination`.

Cada aresta conecta dois nós, e é possível se mover bidirecionalmente entre os nós conectados. Retorne `true` se existir um caminho de `source` a `destination` e `false` caso contrário.

### Exemplo

**Entrada:**
```plaintext
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
```

**Saída:**
```plaintext
true
```

**Explicação:**  
Existe um caminho entre o nó 0 e o nó 2.

### Restrições

- \( 2 <= n <= 2 \times 10^5 \)
- \( 0 <= edges.length <= 2 \times 10^5 \)
- \( edges[i].length == 2 \)
- \( 0 <= u, v < n \)
- \( u != v \)
- \( source != destination \)
- Não há arestas duplicadas.