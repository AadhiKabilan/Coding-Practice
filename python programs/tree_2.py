from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

tree=defaultdict(list)

n=int(input())
parent=[int(input()) for _ in range(n)] # 0 1 1 2 2
values=[int(input()) for _ in range(n)] # 2 3 6 12 27

for i in range(n):
    if parent[i]!=0:
        tree[parent[i]].append(i+1)

sum_of_sub=[]
print("Dfs: ")
def dfs(u):
    print(u)
    for v in tree[u]:
        dfs(v)

dfs(1)

def sub_sum(u):
    total= values[u]
    for v in tree[u]:
        total+=sub_sum(v)
    sum_of_sub[u]=total

sub_sum(1)
print()
print(sum_of_sub)
print(dict(tree))

print(parent,"\n",values)