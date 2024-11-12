# Course Schedule (Problema 207)

**Problema disponível no LeetCode:** [Course Schedule](https://leetcode.com/problems/course-schedule/)

## Descrição do Problema

Você tem um total de `numCourses` cursos para fazer, rotulados de `0` a `numCourses - 1`. É fornecido um array `prerequisites`, onde cada elemento `prerequisites[i] = [ai, bi]` indica que você deve concluir o curso `bi` antes de fazer o curso `ai`.

Por exemplo, o par `[0, 1]` indica que, para cursar o curso `0`, é necessário ter concluído o curso `1` primeiro.

O objetivo é determinar se é possível concluir todos os cursos dados esses pré-requisitos. Retorne `true` se for possível, e `false` caso contrário.

### Exemplos

**Exemplo 1**

**Entrada:**
```plaintext
numCourses = 2, prerequisites = [[1,0]]
```

**Saída:**
```plaintext
true
```

**Explicação:**  
Existem dois cursos no total. Para fazer o curso `1`, é necessário primeiro fazer o curso `0`. Portanto, é possível concluir todos os cursos.

**Exemplo 2**

**Entrada:**
```plaintext
numCourses = 2, prerequisites = [[1,0],[0,1]]
```

**Saída:**
```plaintext
false
```

**Explicação:**  
Existem dois cursos no total. Para fazer o curso `1`, é necessário primeiro fazer o curso `0`, e para fazer o curso `0`, é necessário fazer o curso `1` primeiro. Isso cria uma dependência circular, tornando impossível concluir todos os cursos.

### Restrições

- \(1 <= numCourses <= 2000\)
- \(0 <= \text{prerequisites.length} <= 5000\)
- `prerequisites[i].length == 2`
- \(0 <= a_i, b_i < numCourses\)
- Todos os pares `prerequisites[i]` são únicos.