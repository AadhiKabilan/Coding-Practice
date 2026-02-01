from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

n = 4
parent = [0, 0, 1, 1, 2]

tree = defaultdict(list)
for i in range(1, n+1):
    if parent[i] != 0:
        tree[parent[i]].append(i)

for i,j in enumerate(tree):
    print(i,j)

print(tree)   
 
def dfs(u):
    print(u)
    for v in tree[u]:
        dfs(v)

dfs(1)
