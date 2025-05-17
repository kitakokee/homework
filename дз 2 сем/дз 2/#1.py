#1. Доделать алгоритм Эдмондса — Карпа

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

def bfs_find_path(G, queue, start, visited, flow, capacity):
    queue.add(start)
    visited[start] = True
    parent = {}  
    parent[start] = None

    while queue.head:
        current = queue.remove()
        for i in G[current]:
            if not visited[i] and capacity[(current, i)] - flow[(current, i)] > 0:
                queue.add(i)
                visited[i] = True
                parent[i] = current  



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
