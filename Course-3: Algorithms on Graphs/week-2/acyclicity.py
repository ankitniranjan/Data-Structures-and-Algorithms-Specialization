#Uses python3

import sys

def explore(adj, x, visited):
    for i in adj[x]:
        if not visited[i]:
            visited[i] = True
            explore(adj, i, visited)
    return visited

def acyclic(adj):
    no_of_cycles = 0
    for i in range(len(adj)):
        visited = [False] * len(adj)
        explore(adj, i, visited)
        if visited[i]:
            no_of_cycles += 1
    return (1 if no_of_cycles > 0 else 0)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
