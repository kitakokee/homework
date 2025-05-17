#2. В графе G= (V,E) множество C ⊂E называется рёберным покрытием, если каждая вершина из V
инцидентна по крайней мере одному ребру из C. Предложите алгоритм поиска минимального рёберного
покрытия в двудольном графе за O(VE)

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self):
        if not self.head:
            return None 
        val = self.head.val
        self.head = self.head.next
        return val

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count +=1
            current = current.next
        return count

def bfs_find_path(G, queue, start, visited, flow, capacity, parent):
    queue.add(start)
    visited[start] = True
    parent[start] = None

    while queue.head:
        current = queue.remove()
        for i in G[current]:
            if not visited[i] and capacity[(current, i)] - flow[(current, i)] > 0:
                queue.add(i)
                visited[i] = True
                parent[i] = current
                if i == sink:
                    return True 
    return False  

def bfs_dist(G, queue, start, dist, flow, capacity):
    queue.add(start)
    dist[start] = 0

    while queue.head:
        current = queue.remove()
        for i in G[current]:
            if not dist[i] and capacity[(current, i)] - flow[(current, i)] > 0:
                queue.add(i)
                dist[i] = dist[current] + 1



def edmonds_karp(graph, source, sink):
    num_vertices = max(max(graph.keys()), max(k for v in graph.values() for k in v.keys())) + 1

    capacity = {}
    flow = {}
    for u in graph:
        for v in graph[u]:
            capacity[(u, v)] = graph[u][v]
            flow[(u, v)] = 0
    
    max_flow = 0
    
    while True:
        queue = Deque()
        visited = {i: False for i in graph}
        parent = {}  # Добавим словарь parent
        
        if not bfs_find_path(graph, queue, source, visited, flow, capacity, parent):
            break  
        
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[(parent[s], s)] - flow[(parent[s], s)])
            s = parent[s]

        s = sink
        while s != source:
flow[(parent[s], s)] += path_flow
            flow[(s, parent[s])] -= path_flow
            s = parent[s]

        max_flow += path_flow
            
    return flow, max_flow


def min_edge_cover_bipartite(graph):

    left_nodes = set()
    right_nodes = set()
    edges = []

    for node in graph:
        for neighbor in graph[node]:
            if node not in right_nodes and neighbor not in left_nodes:
                left_nodes.add(node)
                right_nodes.add(neighbor)
                edges.append((node, neighbor)) 

    flow_graph = {}
    source = 'source'
    sink = 'sink'

    flow_graph[source] = {}
    for node in left_nodes:
        flow_graph[source][node] = 1
        if node not in flow_graph:
            flow_graph[node] = {}
        flow_graph[node][source] = 0


    for u, v in edges:
      if u in left_nodes and v in right_nodes:
        if u not in flow_graph:
            flow_graph[u] = {}
        flow_graph[u][v] = 1
        if v not in flow_graph:
            flow_graph[v] = {}
        flow_graph[v][u] = 0

    for node in right_nodes:
        flow_graph[node][sink] = 1
        if sink not in flow_graph:
            flow_graph[sink] = {}
        flow_graph[sink][node] = 0
    

    flow, max_flow = edmonds_karp(flow_graph, source, sink)


    min_cover = set()
    for u, v in edges:
      if u in left_nodes and v in right_nodes and flow[(v, u)] > 0:
        min_cover.add((u, v))

    return min_cover



cover = min_edge_cover_bipartite(graph)
print("минимальное реберное покрытие:", cover)
