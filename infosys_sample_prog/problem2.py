# Problem 2 starter: segment tree for gcd + basic logic
import sys
import math
sys.setrecursionlimit(2000000)

def build_seg(b):
    n = len(b)-1
    size = 1
    while size < n: size <<= 1
    seg = [0]*(2*size)
    for i in range(n):
        seg[size+i] = b[i+1]  # b is 1-indexed
    for i in reversed(range(1, size)):
        seg[i] = math.gcd(seg[2*i], seg[2*i+1])
    return seg, size

def seg_update(seg, size, pos, val):
    i = size + pos - 1
    seg[i] = val
    i >>= 1
    while i:
        seg[i] = math.gcd(seg[2*i], seg[2*i+1])
        i >>= 1

def seg_all_gcd(seg):
    return seg[1]

def readints():
    return list(map(int, sys.stdin.readline().split()))

# Example usage wrapper - adapt I/O format as needed
data = sys.stdin.read().strip().split()
if not data:
    print(0)
    sys.exit(0)
it = iter(data)
n = int(next(it))
a = [0]*(n+1)
for i in range(1, n+1):
    a[i] = int(next(it))
p = int(next(it))
q = int(next(it))
queries = []
for _ in range(q):
    idx = int(next(it)); val = int(next(it))
    queries.append((idx, val))

# prepare b: b[i] = a[i]//p if divisible else 0
b = [0]*(n+1)
cnt_div = 0
for i in range(1, n+1):
    if a[i] % p == 0:
        b[i] = a[i] // p
        cnt_div += 1
    else:
        b[i] = 0

seg, size = build_seg(b)

ans_yes = 0
for (idx, val) in queries:
    # update a[idx] -> val
    # update b and seg
    old_div = (a[idx] % p == 0)
    a[idx] = val
    new_div = (a[idx] % p == 0)
    if old_div and not new_div:
        cnt_div -= 1
        b[idx] = 0
        seg_update(seg, size, idx, 0)
    elif (not old_div) and new_div:
        cnt_div += 1
        b[idx] = a[idx] // p
        seg_update(seg, size, idx, b[idx])
    elif new_div:
        b[idx] = a[idx] // p
        seg_update(seg, size, idx, b[idx])
    # evaluate condition
    if cnt_div == 0:
        res = False
    else:
        g_all = seg_all_gcd(seg)
        if cnt_div < n:
            res = (g_all == 1)
        else:
            # cnt_div == n: need proper subset (size < n)
            # quick check: any element equals p (i.e., b[i]==1)
            if any(x == 1 for x in b[1:]):
                res = True
            else:
                # fallback: compute prefix/suffix gcds O(n) (works but O(n*q) worst-case)
                pref = [0]*(n+2)
                suff = [0]*(n+2)
                for i in range(1, n+1):
                    pref[i] = math.gcd(pref[i-1], b[i])
                for i in reversed(range(1, n+1)):
                    suff[i] = math.gcd(suff[i+1], b[i])
                res = False
                for i in range(1, n+1):
                    g_exc = math.gcd(pref[i-1], suff[i+1])
                    if g_exc == 1:
                        res = True
                        break
    if res:
        ans_yes += 1

print(ans_yes)
