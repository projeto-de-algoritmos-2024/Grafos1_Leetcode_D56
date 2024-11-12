# Find the Town Judge

**Problema disponível no LeetCode:** [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)

## Descrição

Em uma cidade, existem \( n \) pessoas rotuladas de \( 1 \) a \( n \). Há um boato de que uma dessas pessoas é secretamente o juiz da cidade.

Se o juiz da cidade existir, ele deve satisfazer as seguintes condições:

1. O juiz da cidade não confia em ninguém.
2. Todos (exceto o juiz da cidade) confiam no juiz da cidade.
3. Há exatamente uma pessoa que satisfaz as propriedades 1 e 2.

Você recebe um array `trust`, onde `trust[i] = [a_i, b_i]` representa que a pessoa \( a_i \) confia na pessoa \( b_i \). Se uma relação de confiança não existir no array `trust`, então essa relação de confiança não existe.

Retorne o rótulo da pessoa que é o juiz da cidade, caso exista e possa ser identificado, ou retorne `-1` caso contrário.

### Exemplo 1:

**Entrada:**
```plaintext
n = 2, trust = [[1, 2]]
```

**Saída:**
```plaintext
2
```

**Explicação:**  
A pessoa 1 confia na pessoa 2, e a pessoa 2 não confia em ninguém, então a pessoa 2 é o juiz da cidade.

### Exemplo 2:

**Entrada:**
```plaintext
n = 3, trust = [[1, 3], [2, 3]]
```

**Saída:**
```plaintext
3
```

**Explicação:**  
A pessoa 1 e a pessoa 2 confiam na pessoa 3, mas a pessoa 3 não confia em ninguém. Então, a pessoa 3 é o juiz da cidade.

### Exemplo 3:

**Entrada:**
```plaintext
n = 3, trust = [[1, 3], [2, 3], [3, 1]]
```

**Saída:**
```plaintext
-1
```

**Explicação:**  
Neste caso, a pessoa 3 confia em 1, e a pessoa 1 confia em 3. Portanto, ninguém é o juiz da cidade, pois o juiz da cidade não deve confiar em ninguém.

### Restrições

- \( 1 <= n <= 1000 \)
- \( 0 <= trust.length <= 10^4 \)
- \( trust[i].length == 2 \)
- Todos os pares de confiança são únicos.
- \( a_i != b_i \)
- \( 1 <= a_i, b_i <= n \)

## Solução

Para resolver este problema, podemos usar uma abordagem de contagem baseada nas duas condições principais:

1. O juiz não deve confiar em ninguém, então ele terá 0 saídas de confiança.
2. Todos devem confiar no juiz, então ele terá \( n - 1 \) entradas de confiança.

