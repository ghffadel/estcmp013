# Implementação do algoritmo de Floyd-Warshall
# Argumentos: matriz de adjacência, número de vértices
def floyd_warshall (graph, vertices):
    # Matriz de distâncias
    distances = graph.copy()
    
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                # Verifica se a distância de i até j passando por k é menor que a distância direta entre i e j
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]