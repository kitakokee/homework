#3. Есть n предприятий и n банков, предприятия могут брать кредиты у банков (причём одно предприятие может брать кредиты в нескольких банках и наоборот, один банк может давать кредиты нескольких предприятиям). Известно, что i-е предприятие хочет взять в кредит суммарно ai рублей, а j-й банк готов предоставить кредитов суммарно на bj рублей. Могут ли предприятия взять кредиты так, чтобы все условия выполнились

def dfs(G,visited,start):
        visited.append(start)
        for i in G[start]:
            if i not in visited:
                dfs(G,visited,i)


def can_companies_get_loans_with_connections(n, a, b, connections):

graph = {}
  for i in range(n):  
    for j in range(n): 
      if connections[i][j]:
        if i not in graph:
          graph[i] = []
        if (n + j) not in graph:
          graph[n + j] = []
        graph[i].append(n + j)
        graph[n + j].append(i)


  visited = set()
  components = []
  for i in range(2 * n):
    if i not in visited:
      component = set()
      dfs(graph, component, i)
      components.append(component)
      visited.update(component)

    demand_in_component = 0
    supply_in_component = 0

    for node in component:
      if node < n:  
        demand_in_component += a[node]
      else: 
        supply_in_component += b[node - n]

    if demand_in_component > supply_in_component:
      return False  
  return True  

if can_companies_get_loans_with_connections(n, a, b, connections):
  print("могут получить кредиты")
else:
  print("не могут получить кредиты")