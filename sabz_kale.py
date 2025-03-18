n, q = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

serkei_nodes = set(range(1, n + 1))  
distances = []

for i in range(n + 1):
    dist = [-1] * (n + 1)
    dist[i] = 0
    queue = [i]
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    distances.append(dist)

for _ in range(q):
    query = input().split()
    if query[0] == '1':
        v = int(query[1])
        if v in serkei_nodes:
            serkei_nodes.remove(v)
        else:
            serkei_nodes.add(v)
    else:
        brown_list = list(serkei_nodes)
        total_distance = 0
        for i in range(len(brown_list)):
            for j in range(i + 1, len(brown_list)):
                u = brown_list[i]
                v = brown_list[j]
                total_distance += distances[u][v]
        print(total_distance)
