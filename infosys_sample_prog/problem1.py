# Problem 1: Tree Beauty - DSU-on-tree + square-free reduction
import sys
sys.setrecursionlimit(3000000)
MOD = 10**9 + 7

def sieve_primes(limit):
    sieve = [True]*(limit+1)
    primes = []
    for p in range(2, limit+1):
        if sieve[p]:
            primes.append(p)
            step = p
            for q in range(p*p, limit+1, step):
                sieve[q] = False
    return primes

PRIMES = sieve_primes(31623)  # sqrt(1e9) ≈ 31623

def square_free(x):
    res = 1
    v = x
    for p in PRIMES:
        if p*p > v:
            break
        cnt = 0
        while v % p == 0:
            v //= p
            cnt ^= 1   # only parity matters
        if cnt:
            res *= p
    if v > 1:
        # remaining prime factor (exponent 1)
        res *= v
    return res

# Read input (flexible for the formats shown)
data = sys.stdin.read().strip().split()
if not data:
    print(0)
    sys.exit(0)
it = iter(data)
n = int(next(it))
par = [0]*(n+1)
for i in range(1, n+1):
    par[i] = int(next(it))
a = [0]*(n+1)
for i in range(1, n+1):
    a[i] = int(next(it))

# build tree (root: node with par==0; usually node 1)
children = [[] for _ in range(n+1)]
root = 1
for i in range(1, n+1):
    if par[i] == 0:
        root = i
    else:
        children[par[i]].append(i)

# precompute square-free parts
b = [0]*(n+1)
for i in range(1, n+1):
    b[i] = square_free(a[i])

# DSU-on-tree (small-to-large)
beauty_sum = 0

def dfs(u):
    # returns (counter_dict, pairs_count_in_subtree_u)
    # counter: {squarefree_value: count}
    big = {}
    pairs = 0
    for v in children[u]:
        small, small_pairs = dfs(v)
        # small_pairs already counts beauty inside child's subtree; add it in building up
        pairs += small_pairs
        # ensure big is larger
        if len(small) > len(big):
            big, small = small, big
        # merge small into big
        for key, cnt in small.items():
            prev = big.get(key, 0)
            pairs += prev * cnt
            big[key] = prev + cnt
    # add current node's value
    cur = b[u]
    prev = big.get(cur, 0)
    pairs += prev
    big[cur] = prev + 1
    return big, pairs

# Do DFS from root; but tree might have single root par==0. We assume single-rooted as in problem.
_, total = dfs(root)

# But total returned is beauty(root) only. We need sum over all nodes.
# To gather beauties for all nodes, we modified dfs to add small_pairs and return pairs per subtree,
# and in the merging we accumulated pairs from children as part of returned pairs for parent.
# The value `total` is beauty(root). To get sum over all nodes, we should accumulate beauty[u] inside dfs.
# Let's redo with accumulation of sum_beauties as global.

beauty_sum = 0
def dfs2(u):
    global beauty_sum
    big = {}
    pairs = 0
    for v in children[u]:
        small, small_pairs = dfs2(v)
        pairs += small_pairs
        if len(small) > len(big):
            big, small = small, big
        for key, cnt in small.items():
            prev = big.get(key, 0)
            pairs += prev * cnt
            big[key] = prev + cnt
    cur = b[u]
    prev = big.get(cur, 0)
    pairs += prev
    big[cur] = prev + 1
    beauty_sum += pairs
    return big, pairs

dfs2(root)
print(beauty_sum % MOD)
