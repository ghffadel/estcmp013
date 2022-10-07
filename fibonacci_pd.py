# Implementação com PD de Fibonacci
def fibonacci (n):
    # Lista de resultados
    results = [0 for i in range(n + 1)]
    
    # Casos-base
    results[0] = 1
    results[1] = 2
    
    for i in range(2, n + 1):
        # Utilização dos resultados que foram calculados e armazenados
        results[i] = results[i - 1] + results[i - 2]
    
    # Retorna o resultado para n
    return results[n]