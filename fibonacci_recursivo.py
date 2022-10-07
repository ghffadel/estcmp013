# Implementação recursiva de Fibonacci
def fibonacci (n):
    # Verifica os casos-base
    if n == 0:
        return 0
        
    elif n == 1:
        return 1
    
    # Caso não seja um caso-base, há novas chamadas recursivas    
    elif n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)