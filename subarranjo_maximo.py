# Importando o valor "infinito"
from sys import maxsize

# Define o valor para o infinito
INF = maxsize

# Função para encontrar o subarranjo máximo que passa pelo ponto médio
# Argumentos - A: arranjo, low: posição de início, mid: posição do meio, high: posição do fim
def find_max_crossing_subarray (A, low, mid, high):
    # A soma do lado esquerdo começa com o menor valor possível
    left_sum = -INF
    # Inicialização da soma atual
    sum = 0
    
    # Loop por todos os valores do lado esquerdo, do meio para o início
    for i in range(mid, low - 1, - 1):
        # Atualiza a soma atual
        sum += A[i]
        
        # Verifica se a soma atual é maior que a maior soma atual do lado esquerdo
        if sum > left_sum:
            # Caso seja, atualiza o valor da soma do lado esquerdo
            left_sum = sum
            # E atualiza a posição de início do subarranjo máximo
            max_left = i
    
    # A soma do lado direito começa com o menor valor possível   
    right_sum = -INF
    # Inicialização da soma atual
    sum = 0
    
    # Loop por todos os valores do lado direito, do meio para o fim
    for j in range(mid + 1, high + 1):
        # Atualiza a soma atual
        sum += A[j]
        
        # Verifica se a soma atual é maior que a maior soma atual do lado direito
        if sum > right_sum:
            # Caso seja, atualiza o valor da soma do lado direito
            right_sum = sum
            # E atualiza a posição do fim do subarranjo máximo
            max_right = j
    
    # Retorna a tupla de resposta
    # max_left: posição de início do subarranjo máximo, max_right: posição do fim do subarranjo máximo, left_sum + right_sum: soma dos valores do subarranjo máximo
    return (max_left, max_right, left_sum + right_sum)

# Função principal que encontra um subarranjo máximo dentro do arranjo A
# Argumentos - A: arranjo, low: posição de início, high: posição do fim 
def find_maximum_subarray (A, low, high):
    # Verifica se o subarranjo atual tem tamanho 1
    if high == low:
        # Se sim, retorna o subarranjo atual
        return (low, high, A[low])
    
    # Caso contrário...
    else:
        # Calcula o ponto médio
        mid = (low + high) // 2
        
        # Divide o problema em dois subproblemas
        # Calcula a solução pro lado esquerdo
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        # E pro lado direito
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
        # Verifica o caso do subarranjo máximo que passa pelo ponto médio
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        
        # Verifica qual dos subarranjos é o máximo global e o retorna
        # Verificação do subarranjo esquerdo
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        
        # Verificação do subarranjo direito
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        
        # Se nem o esquerdo nem o direito são os subarranjos máximos, então só pode ser o que passa pelo ponto médio
        else:
            return (cross_low, cross_high, cross_sum)