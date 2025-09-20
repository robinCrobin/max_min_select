# max_min_select

## Descrição do Projeto

Este projeto implementa o algoritmo de seleção simultânea do maior e do menor elemento (MaxMin Select) de uma sequência de números, utilizando a abordagem de divisão e conquista.

### Explicação do Algoritmo

1. **Divisão**: A lista é dividida em duas partes aproximadamente iguais.
2. **Conquista**: Recursivamente, o maior e o menor elemento são encontrados em cada parte.
3. **Combinação**: Os resultados são combinados para determinar o maior e o menor elemento global.

### max_min_select(arr)

```python
def max_min_select(arr):
```

- Define a função `max_min_select` que recebe um array `arr` como argumento. Esta função é responsável por encontrar o maior e o menor elemento do array.

```python
    def recursive_max_min(arr, low, high):
```

- Define uma função interna `recursive_max_min` que recebe dois índices, `low` e `high`, que representam os limites inferior e superior da parte do array que está sendo considerada.

```python
        if low == high:
            return arr[low], arr[low]
```

- Caso base: Se `low` e `high` são iguais, significa que há apenas um elemento na parte do array considerada. Nesse caso, tanto o maior quanto o menor elemento são o próprio elemento.

```python
        elif high == low + 1:
            if arr[low] < arr[high]:
                return arr[low], arr[high]
            else:
                return arr[high], arr[low]
```

- Caso base: Se há exatamente dois elementos, a função compara os dois e retorna o menor e o maior.

```python
        else:
            mid = (low + high) // 2
            min1, max1 = recursive_max_min(arr, low, mid)
            min2, max2 = recursive_max_min(arr, mid + 1, high)
```

- Caso recursivo: Divide o array em duas partes, calculando o índice do meio `mid`. Chama recursivamente `recursive_max_min` para cada metade do array.

```python
            return min(min1, min2), max(max1, max2)
```

- Combina os resultados das duas metades. O menor elemento global é o menor entre os menores das duas metades, e o maior elemento global é o maior entre os maiores das duas metades.

```python
    if not arr:
        return None, None
```

- Verifica se o array está vazio. Se estiver, retorna `None` para ambos o menor e o maior elemento, pois não há elementos para comparar.

```python
    return recursive_max_min(arr, 0, len(arr) - 1)
```

- Inicia a recursão chamando `recursive_max_min` com os índices que cobrem todo o array.

## Como Executar o Projeto

### Dependências

- Python 3.13.0

## Clone o repositório

```bash
git clone https://github.com/robinCrobin/max_min_select.git
```

## Executar o Script

Execute o script principal:

```bash
python3 main.py
```

ou

```bash
python main.py
```

Digite a quantidade de números que serão comparados e sem seguida os números, enviando eles 1 a 1.

```bash
Digite a quantidade de números na lista:
```

## Relatório técnico

## Análise da Complexidade Assintótica

1. **Divisão do Problema**:

   - O algoritmo divide a lista de \( n \) elementos em duas sublistas de aproximadamente \( n/2 \) elementos

2. **Conquista (Recursão)**:

   - Para cada sublista, o algoritmo é chamado recursivamente.
   - Se a sublista tem apenas um elemento, não há comparações. (Caso base 1)
   - Se a sublista tem dois elementos, uma comparação é feita para determinar o maior e o menor. (Caso base 2)
   - Para sublistas maiores, o processo é repetido até que se chegue aos casos base (um ou dois elementos).

3. **Combinação dos Resultados**:
   - Após resolver os subproblemas, os resultados são combinados.
   - Para combinar os resultados de duas sublistas, são necessárias duas comparações:
     - Uma comparação para determinar o menor entre os dois menores das sublistas.
     - Uma comparação para determinar o maior entre os dois maiores das sublistas.

#### Cálculo do Total de Comparações

- **Número de Comparações na Combinação**:

  - Para cada nível de recursão, duas comparações são feitas para cada par de sublistas.
  - Como a lista é dividida em duas partes em cada nível, o número de pares de sublistas é \( n/2 \).

- **Número Total de Comparações**:
  \[
  C(n) = 2C(n/2) + 2
  \]

  - Onde \( 2C(n/2) \) representa as comparações feitas nas sublistas e \( 2 \) são as comparações feitas na combinação.

- **Resolvendo a Recorrência**:
  - A solução para esta recorrência é \( C(n) = 3n/2 - 2 \).

### Complexidade Temporal \( O(n) \)

- O número total de comparações é linear em relação ao número de elementos \( n \), ou seja, \( C(n) = 3n/2 - 2 \).
- Portanto, a complexidade temporal do algoritmo é \( O(n) \), pois o fator dominante é linear.

## Análise da Complexidade Assintótica pela Aplicação do Teorema Mestre

Considere a recorrência do MaxMin Select:

\[ 𝑇(𝑛) = 2𝑇 (𝑛 / 2) + 𝑂(1)\]

### Perguntas:

1. **Identifique os valores de \( a \), \( b \) e \( f(n) \) na fórmula:**

- A fórmula geral do Teorema Mestre é:
  \[𝑇(𝑛) = 2𝑇 (𝑛 / 2) + 𝑂(1)\]
- \( a = 2 \): Número de subproblemas.
- \( b = 2 \): Fator de redução do tamanho do problema.
- \( O(1) \): Custo de combinar os resultados dos subproblemas.

2. **Calcule \( \log_b a \) para determinar o valor de \( p \):**

   - \( log₂2 = 1 \)

3. **Determine em qual dos três casos do Teorema Mestre esta recorrência se enquadra:**

   - **Caso 1**: 𝑓(𝑛) = 𝑂(𝑛log_b(a) − 𝜖 ), para algum 𝜖 > 0.
   - **Caso 2**: 𝑓(𝑛) = Θ(𝑛log_b(a) )
   - **Caso 3**: 𝑓(𝑛) = Ω(𝑛log_b(a) + 𝜖 ), para algum 𝜖 > 0, e é necessário que 𝑎𝑓(𝑛 / 𝑏) ≤ 𝑐𝑓(𝑛), para 𝑐 < 1 e 𝑛 suficientemente grande
   - Para o MaxMin Select, \( f(n) = O(1) que é O(n0) \) e \( \log_b(a) = 1 \), então estamos no **Caso 1 (0 < 1)**.

4. **Encontre a solução assintótica \( T(n) \) da fórmula:**
   - De acordo com o **Caso 1** do Teorema Mestre:
     𝑇(𝑛) = Θ (𝑛log_b(a) )
     T(n)=Θ(n^log_b(a))=Θ(n^1)=Θ(n)

Portanto, a solução assintótica da recorrência é \( T(n) = O(n) \), confirmando que o algoritmo é linear em relação ao número de elementos \( n \).