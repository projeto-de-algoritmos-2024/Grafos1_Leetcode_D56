# Shortest Cycle in a Graph

**Problema disponível no LeetCode:** [Shortest Cycle in a Graph](https://leetcode.com/problems/shortest-cycle-in-a-graph/)

## Descrição

Dado um grafo não-direcionado representado por \( n \) nós (numerados de 0 a \( n - 1 \)) e uma lista de arestas, encontre o comprimento do ciclo mais curto no grafo. Se não houver ciclo, retorne -1.

Um **ciclo** é uma sequência de nós onde o primeiro e o último nó são o mesmo, e cada par consecutivo de nós é uma aresta no grafo. O comprimento de um ciclo é o número de arestas que ele contém.

### Exemplo

**Entrada:**
```plaintext
n = 7
edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
```

**Saída:**
```plaintext
3
```

**Explicação:**  
O grafo possui um ciclo de comprimento 3: `0 → 1 → 2 → 0`.

### Restrições

- \( 2 <= n <= 1000 \)
- \( 1 <= edges.length <= 1000 \)
- \( edges[i].length == 2 \)
- \( 0 <= u, v < n \)
- \( u != v \)
- Não há arestas duplicadas.

## Solução

Para resolver este problema, é possível utilizar a **Busca em Largura (BFS)** para encontrar o ciclo mais curto em um grafo não-direcionado. A ideia principal é iniciar uma busca a partir de cada nó, procurando o ciclo mais curto possível.





