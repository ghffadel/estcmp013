# Implementação bottom-up do LCS
def lcs (X, Y, m, n):
    # Criação da tabela de respostas
    results = [[0 for j in range(n + 1)] for i in range(m + 1)]
        
    # Preenchimento da tabela de respostas
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Se os últimos caracteres forem iguais, utiliza-se a resposta anterior + 1 
            if X[i - 1] == Y[j - 1]:
                results[i][j] = results[i - 1][j - 1] + 1
              
            # Se forem diferentes, utiliza-se a maior entre as respostas anteriores 
            else:
                results[i][j] = max(results[i - 1][j], results[i][j - 1])
    
    # Retorna a resposta para m e n            
    return results[m][n]