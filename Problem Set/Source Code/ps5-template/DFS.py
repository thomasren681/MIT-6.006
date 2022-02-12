from UndGraphGenerator import random_graph_generator
from UndGraphGenerator import two_connected_components_example
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def DFS(Adj, s, parent = None, order = None):
    '''
    :param Adj: adjacency list
    :param s: source node
    :param parent: parent list
    :param order: finishing order
    :return: parent, order
    '''
    if parent is None:
        parent = [None for v in Adj]
        parent[s] = s
        order = []
    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            DFS(Adj,v,parent,order)
    order.append(s)
    return parent,order


def full_DFS(Adj):
    parent = [None for v in Adj]
    order = []
    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = None
            DFS(Adj, v, parent, order)
    return parent, order

if __name__=='__main__':
    num_nodes = 7
    G, Adj = two_connected_components_example()
    print(Adj)
    nx.draw(G,with_labels=True)

    parent, order = full_DFS(Adj)
    print('parent:',parent)
    print('finishing order:',order)

    plt.show()
