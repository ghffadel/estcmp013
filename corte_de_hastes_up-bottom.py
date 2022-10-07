# Implementação up-bottom do algoritmo do corte de hastes
def cut_rod (prices, n):
    # Caso-base, onde para o tamanho igual a 0 não há como dividi-lo
    if n == 0:
        return 0
    
    # A resposta começa com o menor valor possível
    answer = -infinity
    
    # Para cada i de 1 até n
    for i in range(1, n + 1):
        # Compara-se a resposta atual com a receita que se obtém ao se dividir a hasste na posição i
        answer = max(answer, prices[i] + cut_rod(prices, n - i))
      
    # Retorna a resposta 
    return answer