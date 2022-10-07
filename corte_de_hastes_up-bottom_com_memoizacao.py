# Definindo o valor infinito
infinity = float('inf')
  
# Implementação up-bottom com memoização do algoritmo do corte de hastes 
def cut_rod (prices, n, memoization = None):
    # Se a tabela de memoização não for passada no parâmetro, há a criação de uma com todas as posições tendo o menor valor possível.
    if memoization is None:
       memoization = [-infinity for i in range(n + 1)]

    # Verifica a lista de memoização se o problema já foi resolvido anteriormente para o tamanho n
    if memoization[n] != -infinity:
        return memoization[n]
    
    # Quando o tamanho da haste é 0, não há como dividi-la  
    if n == 0:
        answer = 0
    
    else:
        # A resposta começa com o menor valor possível
        answer = -infinity
        
        # Para cada i de 1 até n
        for i in range(1, n + 1):
            # Compara-se a resposta atual com a receita que se obtém ao se dividir a haste na posição i
            answer = max(answer, prices[i] + cut_rod(prices, n - i, memoization))
    
    # Armazena a resposta encontrada para o tamanho n na lista de memoização      
    memoization[n] = answer
    
    # Retorna a resposta
    return answer