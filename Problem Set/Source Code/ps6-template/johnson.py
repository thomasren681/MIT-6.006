INF = 99999     # distance magnitudes will not be larger than this number

def convert_S_to_Adj_and_w(n,S):
    Node_list = [i for i in range(n)]
    # print(Node_list)

    # Initialize Adj and w
    Adj,w = {},{}
    for node in Node_list:
        Adj[node] = []
        w[node] = {}

    # Convert edges to Adj and w
    for (u,v,weight) in S:
        Adj[u].append(v)
        w[u][v] = weight

    return Adj,w

def johnson(n, S):
    '''
    Input:  n | Number of vertices in the graph
            S | Tuple of triples (u, v, w) representing edge (u, v) of weight w
    Output: D | Tuple of tuples where D[u][v] is the distance from u to v
              |   or INF if v is not reachable from u
              |   or None if the input graph contains a negative-weight cycle
    '''
    D = [[INF for _ in range(n)] for _ in range(n)]
    ##################
    # YOUR CODE HERE #
    # Build Adjacency and w data structure
    Adj,W = convert_S_to_Adj_and_w(n,S)
    def w(u,v):
        return W[u][v]

    # Add a super node and connect them
    Node_list = [i for i in range(n)]
    Adj[n] = Node_list
    W[n] = {}
    for node in Node_list:
        W[n][node] = 0

    # Compute h[u] for node u using Bellman-Ford
    if bellman_ford(Adj,w,n) is None:
        return None
    else:
        h, _ = bellman_ford(Adj,w,n)

    # Reweight the graph
    for u in W:
        for v in W[u]:
            W[u][v] += h[u]-h[v]

    # Delete our super node
    del W[n]
    Adj.pop(n)
    # Use dijkstra to conpute shortest path and reweight back
    for u in W:
        d,_ = dijkstra(Adj,w,u)
        for v in range(len(d)):
            if d[v] != INF:
                d[v] += h[v] - h[u]
                D[u][v] = d[v]


    ##################
    D = tuple(tuple(row) for row in D)
    return D

####################################
# USE BUT DO NOT MODIFY CODE BELOW #
####################################
def bellman_ford(Adj, w, s):    # from R12
    '''
    Input: Adj | Direct access array mapping a vertex to a list of adjacencies
             w | Function w(u, v): weight of the edge from u to v
             s | Vertex where 0 <= s < |Adj|
    Output:  d | Direct access array mapping a vertex to distance from s
               |   or INF if v is not reachable from u
               |   or None if the input graph contains a negative-weight cycle
        parent | Direct access array mapping a vertex to parent on shortest path
    '''
    d = [INF for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, None
    V = len(Adj)
    for k in range(V - 1):
        for u in range(V):
            for v in Adj[u]:
                if (d[v] > d[u] + w(u, v)) and (d[u] < INF):
                    d[v] = d[u] + w(u, v)
                    parent[v] = u
    for u in range(V):
        for v in Adj[u]:
            if d[v] > d[u] + w(u,v):
                return None
    return d, parent

def dijkstra(Adj, w, s):        # from R13
    '''
    Input: Adj | Direct access array mapping a vertex to a list of adjacencies
             w | Function w(u, v): non-negative weight of the edge from u to v
             s | Vertex where 0 <= s < |Adj|
    Output:  d | Direct access array mapping a vertex to distance from s
               |   or INF if v is not reachable from u
        parent | Direct access array mapping a vertex to parent on shortest path
    '''
    d = [INF for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, None
    Q = PriorityQueue()
    V = len(Adj)
    for v in range(V):
        Q.insert(v, d[v])
    for _ in range(V):
        u = Q.extract_min()
        for v in Adj[u]:
            if (d[v] > d[u] + w(u, v)) and (d[u] < INF):
                d[v] = d[u] + w(u, v)
                parent[v] = u
            Q.decrease_key(v, d[v])
    return d, parent

class Item:
    def __init__(self, label, key):
        self.label, self.key = label, key

class PriorityQueue:
    def __init__(self):
        self.A = []
        self.label2idx = {}

    def min_heapify_up(self, c):            
        if c == 0: return
        p = (c - 1) // 2
        if self.A[p].key > self.A[c].key:   
            self.A[c], self.A[p] = self.A[p], self.A[c]         
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            self.min_heapify_up(p)         

    def min_heapify_down(self, p):          
        if p >= len(self.A): return
        l = 2 * p + 1
        r = 2 * p + 2
        if l >= len(self.A): l = p
        if r >= len(self.A): r = p
        c = l if self.A[r].key > self.A[l].key else r 
        if self.A[p].key > self.A[c].key:             
            self.A[c], self.A[p] = self.A[p], self.A[c]         
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            self.min_heapify_down(c)       

    def insert(self, label, key):
        self.A.append(Item(label, key))
        idx = len(self.A) - 1
        self.label2idx[self.A[idx].label] = idx
        self.min_heapify_up(idx)

    def extract_min(self):
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        self.label2idx[self.A[0].label] = 0
        del self.label2idx[self.A[-1].label]
        min_label = self.A.pop().label
        self.min_heapify_down(0)
        return min_label

    def decrease_key(self, label, key):
        if label in self.label2idx:
            idx = self.label2idx[label]
            if key < self.A[idx].key:
                self.A[idx].key = key
                self.min_heapify_up(idx)

if __name__ == '__main__':
    n = 4
    S = ((0, 1, -1), (0, 2, -2), (1, 3, -5), (2, 1, -3), (2, 3, -4))
    print(johnson(n,S))