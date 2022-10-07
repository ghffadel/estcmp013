# Importando as funções necessárias para a fila de prioridades (heap)
from heapq import heappop, heappush

# Definindo o valor infinito
infinity = float('inf')

# Implementação do algoritmo de Dijkstra
# Argumentos: graph - lista de adjacências do grafo, origin - nó a partir do qual se calcula as distâncias
def dijkstra (graph, origin):
    # Tabela que armazenará as distâncias
    distances = dict()

    # Inicializa todas as distâncias como infinito para cada vértice
    for vertex in graph:
        distances[vertex] = infinity
    
    # A distância da origem para si mesmo é 0
    distances[origin] = 0
    priority_queue = []
    
    # Começa adicionando a origem na fila de prioridades
    heappush(priority_queue, (distances[origin], origin))
    
    # Enquanto a fila não estiver vazia
    while len(priority_queue) > 0:
        # O nó com a menor distância é retirado
        node_distance, node = heappop(priority_queue)
        
        # Verifica os seus filhos
        for child, weight in graph[node]:
            # Se for possível melhorar a distância do filho
            if node_distance + weight < distances[child]:
                # Atualiza-se a distância
                distances[child] = node_distance + weight
                # E adiciona o filho para a fila de prioridades
                heappush(priority_queue, (distances[child], child))
    
    # Retorna a tabela de distâncias            
    return distances