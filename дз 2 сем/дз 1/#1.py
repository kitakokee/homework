#1. Написать функцию, которая проверяет есть ли в графе эйлеров путь, если есть возвращает его
def find_eulerian_path(graph):
    def is_eulerian(graph):
        odd_count = 0
        for v in graph:
            if len(graph[v]) % 2 != 0:
                odd_count += 1
        return odd_count == 0 or odd_count == 2

    def find_start_node(graph):
        start = None
        found = False

        for v in graph:
            if len(graph[v]) % 2 != 0:
                start = v
                found = True
                break

        if not found:
            for v in graph:
                start = v
                break

        return start
    
    def dfs_euler(graph, curr, path):
        while graph[curr]:
            neighbor = graph[curr].pop()

            if neighbor in graph and curr in graph[neighbor]:
               graph[neighbor].remove(curr)
            
            dfs_euler(graph, neighbor, path)

        path.insert(0, curr)

    if not is_eulerian(graph):
        return None

    start = find_start_node(graph)
    path = []

    dfs_euler(graph, start, path)

    return path



def get_graph():
    M = int(input())
    G = {}
    for i in range(M):
        v1, v2, w = input().split()
        w = float(w)
        if v1 in G:
            if v2 in G[v1]:
                pass
            else:
                G[v1][v2] = w
        else:
            G[v1] = {v2: w}
        if v2 in G:
            if v1 in G[v2]:
                pass
            else:
                G[v2][v1] = w
        else:
            G[v2] = {v1: w}
    return G

graph = get_graph()
result = find_eulerian_path(graph)

if result:
    print(result)
else:
    print("Эйлеров путь не существует.")

