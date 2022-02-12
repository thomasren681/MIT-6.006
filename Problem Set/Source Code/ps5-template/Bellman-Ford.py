import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def weight(u,v):
    # weight of edge(u,v)
    return W[u][v]

def try_to_relax(Adj,W,d,parent,u,v):
    if d[v]>d[u]+weight(u,v):
        d[v] = d[u] + weight(u,v)
        parent[v] = u

def bellman_ford(Adj, w, s): # Adj: adjacency list, w: weights, s: start
    # initialization
    infinity = float('inf')             # number greater than sum of all + weights
    d = [infinity for _ in Adj]         # shortest path estimates d(s, v)
    parent = [None for _ in Adj]        # initialize parent pointers
    d[s], parent[s] = 0, s              # initialize source
    # construct shortest paths in rounds
    V = len(Adj)                        # number of vertices
    for k in range(V - 1):              # relax all edges in (V - 1) rounds
        for u in range(V):              # loop over all edges (u, v)
            for v in Adj[u]:            # relax edge from u to v
                try_to_relax(Adj, w, d, parent, u, v)
    # check for negative weight cycles accessible from s
    for u in range(V):                  # Loop over all edges (u, v)
        for v in Adj[u]:
            if d[v] > d[u] + w(u,v):    # If edge relax-able, report cycle
                raise Exception('Ack! There is a negative weight cycle!')
    return d, parent


if __name__=='__main__':
    W = {
        0:{1:2},
        1:{4:1,3:-1,2:-1},
        2:{3:-3},
        3:{4:4},
        4:{}
    }
    Adj = {
        0:[1],
        1:[2,3,4],
        2:[3],
        3:[4],
        4:[]
    }