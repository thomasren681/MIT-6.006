import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from DFS import DFS

def weight(u,v):
    # weight of edge(u,v)
    return W[u][v]

def try_to_relax(Adj,W,d,parent,u,v):
    if d[v]>d[u]+weight(u,v):
        d[v] = d[u] + weight(u,v)
        parent[v] = u

def DAG_relaxation(Adj,W,s):
    _,order = DFS(Adj,s)
    order.reverse()
    d = [float('inf') for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0,s
    for u in order:
        for v in Adj[u]:
            try_to_relax(Adj,W,d,parent,u,v)
    return d,parent


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
    G = nx.DiGraph()
    Node_list = list(np.arange(len(W)))
    # pos = nx.spring_layout(G,seed=42)
    for u in W:
        for v in W[u]:
            G.add_edge(u,v,weight=W[u][v])
    nx.draw(G, with_labels=True,font_weight='bold')
    plt.show()

    d,parent = DAG_relaxation(Adj,W,0)
    print(d)
    print(parent)
