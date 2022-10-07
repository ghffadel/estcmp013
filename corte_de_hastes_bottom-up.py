# Definindo o valor infinito
infinity = float('inf')

# Implementação bottom-up do algoritmo do corte de hastes 
def cut_rod (prices, n):
    # Inicialização da lista que armazena as respostas
    results = [0 for i in range(n + 1)]
    
    # Não há como dividir uma haste de tamanho 0
    results[0] = 0    
    
    # Resolve os problemas indo de 1 até n
    for i in range(1, n + 1):
        # O resultado para i começa com o menor valor possível
        result = -infinity
        
        # Verifica qual é a melhor posição para dividir a haste
        # Usa-se as respostas já calculadas de outros problemas menores
        for j in range(1, i + 1):
            result = max(result, prices[j] + results[i - j])
            
        # Atualiza a lista de respostas com o resultado que foi encontrado
        results[i] = result
    
    # Retorna a resposta para o tamanho n
    return results[n]