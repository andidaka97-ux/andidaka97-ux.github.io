import sys
input = sys.stdin.readline

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)
outdeg = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    outdeg[a] += 1
    indeg[b] += 1

if outdeg[1] - indeg[1] != 1 or indeg[n] - outdeg[n] != 1:
    print("IMPOSSIBLE")
    sys.exit()

for i in range(2, n):
    if indeg[i] != outdeg[i]:
        print("IMPOSSIBLE")
        sys.exit()

stack = [1]
path = []

while stack:
    v = stack[-1]
    if adj[v]:
        stack.append(adj[v].pop())
    else:
        path.append(stack.pop())

path.reverse()

if len(path) != m + 1 or path[-1] != n:
    print("IMPOSSIBLE")
else:
    print(" ".join(map(str, path)))
