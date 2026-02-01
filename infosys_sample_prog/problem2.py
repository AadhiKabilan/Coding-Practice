import sys
import math

# Increase recursion depth for deep segment trees
sys.setrecursionlimit(200000)

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class SegmentTree:
    def __init__(self, data, p):
        self.n = len(data)
        self.p = p
        self.tree = [0] * (4 * self.n)
        self._build(data, 1, 0, self.n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            # Only consider elements divisible by p [cite: 139]
            if data[start] % self.p == 0:
                self.tree[node] = data[start]
            else:
                self.tree[node] = 0
            return
        mid = (start + end) // 2
        self._build(data, 2 * node, start, mid)
        self._build(data, 2 * node + 1, mid + 1, end)
        self.tree[node] = get_gcd(self.tree[2 * node], self.tree[2 * node + 1])

    def update(self, node, start, end, idx, val):
        if start == end:
            if val % self.p == 0:
                self.tree[node] = val
            else:
                self.tree[node] = 0
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = get_gcd(self.tree[2 * node], self.tree[2 * node + 1])

def solve_p2():
    # Reading input as per format [cite: 165-178]
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    p = int(input_data[n+1])
    q = int(input_data[n+2])
    
    # queries start after the 'two' indicator [cite: 174-176]
    query_start = n + 4
    queries = []
    for i in range(q):
        idx = int(input_data[query_start + 2*i])
        val = int(input_data[query_start + 2*i + 1])
        queries.append((idx, val))

    st = SegmentTree(a, p)
    yes_answers = 0

    for idx_1, new_val in queries:
        # idx_1 is 1-indexed [cite: 177]
        st.update(1, 0, n - 1, idx_1 - 1, new_val)
        
        # If the GCD of all multiples of p is exactly p, 
        # a good subsequence exists [cite: 139, 142]
        if st.tree[1] == p:
            yes_answers += 1
            
    print(yes_answers)

if __name__ == "__main__":
    solve_p2()