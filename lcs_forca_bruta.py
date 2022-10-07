# Implementação do LCS usando força bruta
def LCS (X, Y, m, n):
    # Caso-base, quando alguma string está com tamanho 0
    if m == 0 or n == 0:
        return 0
    
    # Se os últimos caracteres de ambas as strings forem iguais, a busca continua descartando-os
    elif X[m - 1] == Y[n - 1];
        return lcs(X, Y, m - 1, n - 1) + 1
        
    # Caso contrário, a resposta será a melhor entre as duas novas buscas
    else:
        return max(lcs(X, Y, m - 1, n) + lcs(X, Y, m, n - 1))
        
