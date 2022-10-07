# Definição da função para resolver o Problema da Mochila
# Argumentos: tamanhos dos itens, valores dos itens, capacidade máxima da mochila
def knapsack (weights, values, maximum_capacity):
    # length = Quantidade de itens
    length = len(weights)
    # Tabela de memoização que armazenará as respostas
    # table[i] = Maior valor que você pode obter em uma mochila com capacidade máxima de i
    table = [0 for i in range(length + 1)]
    
    # Resolução dos subproblemas
    for i in range(1, n + 1):
        for j in range(maximum_capacity, -1, -1):
            # Verifica se é possível incluir o item atual na mochila
            if weights[i - 1] <= j:
                # Se for possível, verifica se é melhor adicionar o item ou não
                table[j] = max(table[j], table[j - weights[i - 1] + values[i - 1]])
    
    # Retorna o resultado levando em consideração a capacidade máxima da mochila 
    return table[maximum_capacity]