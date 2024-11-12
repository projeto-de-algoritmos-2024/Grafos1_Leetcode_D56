Aqui está o README em Markdown para o problema "Longest Cycle in a Graph" no LeetCode.

---

# Longest Cycle in a Graph

**Problema disponível no LeetCode:** [Longest Cycle in a Graph](https://leetcode.com/problems/longest-cycle-in-a-graph/)

## Descrição

Dado um grafo dirigido representado por \( n \) nós (numerados de 0 a \( n - 1 \)) e uma lista onde cada nó aponta para exatamente um nó (ou seja, um grafo dirigido onde cada nó tem no máximo uma saída), encontre o comprimento do ciclo mais longo contido no grafo. Se não houver ciclo, retorne -1.

Um **ciclo** é uma sequência de nós onde o primeiro e o último nó são o mesmo, e cada par consecutivo de nós é uma aresta no grafo. O comprimento de um ciclo é o número de arestas que ele contém.

### Exemplo

**Entrada:**
```plaintext
edges = [3,3,4,2,3]
```

**Saída:**
```plaintext
3
```

**Explicação:**  
O grafo possui um ciclo de comprimento 3: `2 → 4 → 3 → 2`.

### Restrições

- \( 2 <= n <= 10^5 \)
- \( edges.length == n \)
- \(-1 <= edges[i] < n\)
- \( edges[i] != i \), para qualquer índice válido \( i \).

#