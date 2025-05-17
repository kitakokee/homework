#3. В городе есть n пунктов обмены валюты. В связи с глобальным мировым кризисом, вызванным коронавирусом, каждый обменник готов принять только одну валюту и конвертировать её в другую (тоже строго определённую) по своему курсу. Определите, можно ли обладая изначальной суммой в 1 рубль бесконечно обогатиться?

M = int(input())

G = {}

for i in range(M):
    v1,v2,w = input().split()
    w = -float(w)  
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2:w}
    

def bellman_ford(G,start):
    d = {i:float('inf') for i in G}
    d[start] = 0
    for i in range(len(G)-1):
        for node1 in G:  
            for node2 in G[node1]:
                if d[node2] > d[node1] + G[node1][node2]:
                    d[node2] = d[node1] + G[node1][node2]

    for node1 in G:  
        for node2 in G[node1]:
            if d[node2] > d[node1] + G[node1][node2]:

    return False 


if 'A' in G:
  result = bellman_ford(G,'A')
  print(result)
else:
  print(False)