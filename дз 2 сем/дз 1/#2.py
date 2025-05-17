#2. Реализовать алгоритм Джонсона
import heapq

def read_graph():
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

def dijkstra(G, start):
    distances = {i: float('infinity') for i in G}
    distances[start] = 0
    h = [(0, start)]
    while h:
        cur_dist, cur_node = heapq.heappop(h)
        if cur_dist > distances[cur_node]:
            continue
        for neighbor in G[cur_node]:
            distance = cur_dist + G[cur_node][neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(h, (distance, neighbor))
    return distances


def bellman_ford(G, start):
    distances = {i: float('infinity') for i in G}
    distances[start] = 0

    for _ in range(len(G) - 1):
        for u in G:
            for v, weight in G[u].items():
                if distances[u] != float('infinity') and distances[v] > distances[u] + weight:
                    distances[v] = distances[u] + weight

    return distances


def johnson(graph):
    for node in graph:
        graph.setdefault('_s', {})[node] = 0.0

    h = bellman_ford(graph, '_s')
    all_pairs_shortest_paths = {}
    for start_node in graph:
        all_pairs_shortest_paths[start_node] = dijkstra(graph, start_node)

    return all_pairs_shortest_paths


G = read_graph()
result = johnson(G)

for start_node, distances in result.items():
    print(f"расстояние от {start_node} до {distances}")


