#Uses python3

import sys
import numpy as np

sys.setrecursionlimit(200000)

def dfs(adj, visited, postOrder, clock, x):
    visited[x] = True
    for i in adj[x]:
        if not visited[i]:
            dfs(adj, visited, postOrder, clock, i)
    clock[0] += 1
    postOrder[x] = clock[0]
    return

def number_of_strongly_connected_components(adj, adjr):
    result = 0
    #write your code here
    postOrder = [0] * len(adj)
    visited = [False] * len(adj)
    clock = [0]

    for i in range(len(adjr)):
        if not visited[i]:
            dfs(adjr, visited, postOrder, clock, i)

    reversePostOrder = np.argsort(postOrder)[::-1]

    for i in reversePostOrder:
        if not visited[i]:
            result += 1
            dfs(adj, visited, postOrder, clock, i)

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    adjr = [[] for _ in range(n)]
    for (a, b) in edges:
        adjr[b -1].append(a - 1)
    print(number_of_strongly_connected_components(adj, adjr))
