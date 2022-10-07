# Definição da função para resolver o Problema da Mochila
# Argumentos: tamanhos dos itens, valores dos itens, capacidade máxima da mochila
def knapsack (weights, values, maximum_capacity):
    # length = Quantidade de itens
    length = len(weights)
    # Tabela de memoização que armazenará as respostas
    # table[i][j] = Maior valor que você pode obter usando até i itens em uma mochila com capacidade máxima de j
    table = [[0 for j in range(maximum_capacity + 1)] for i in range(length + 1)]
    
    # Resolução dos subproblemas
    for i in range(1, length + 1):
        for j in range(1, maximum_capacity + 1):
            # Verifica se é possível incluir o item atual na mochila
            if weights[i - 1] <= j:
                # Se for possível, verifica se é melhor adicionar o item ou não
                table[i][j] = max(values[i - 1] + table[i - 1][j - weights[i - 1]], table[i - 1][j])
            
            # Se não for possível, utiliza-se o resultado anterior
            else:
                table[i][j] = table[i - 1][j]
    
    # Retorna o resultado levando em consideração todos os itens e a capacidade máxima da mochila 
    return table[length][maximum_capacity]