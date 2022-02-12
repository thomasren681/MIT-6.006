import networkx as nx
import matplotlib.pyplot as plt
from UndGraphGenerator import random_graph_generator

def BFS(Adj, s):
    '''
    :param Adj: map each vertex to its adjacency list
    :param s: statring vertex
    :return: parent and level
    '''
    parent = [None for v in Adj]
    parent[s] = s
    level = [[s]]
    while 0 < len(level[-1]):
        level.append([])
        for u in level[-2]:
            for v in Adj[u]:
                if parent[v] is None:
                    parent[v] = u
                    level[-1].append(v)

    return parent, level

def unweighted_shortest_path(Adj, s, t):
    parent, _ = BFS(Adj, s)
    if parent[t] is None:
        return None
    i = t
    path = [t]
    while i != s:
        i = parent[i]
        path.append(i)
    return path[::-1]

if __name__=='__main__':
    num_nodes = 5
    G, Adj = random_graph_generator(num_nodes,connect_probability=1/num_nodes)
    print(Adj)
    nx.draw(G, with_labels=True)

    s, t = 0,3

    parent, level = BFS(Adj,0)
    print('parent:',parent)
    print('level:',level)
    print('shortest path form %s to %s'%(s,t),unweighted_shortest_path(Adj,s,t))

    plt.show()