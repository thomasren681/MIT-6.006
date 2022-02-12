import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt


def assert_undirected_edge(tuple1,tuple2):
    if tuple1==tuple2 or tuple1 == tuple2[::-1]:
        return True
    else:
        return False

def assert_edges_in(edge,edge_list):
    for edge_stored in edge_list:
        if assert_undirected_edge(edge,edge_stored):
            return True

    return False

def adj_to_edge_list(Adj):
    edge_list = []
    for i, adj_list in enumerate(Adj):
        for j in adj_list:
            edge = tuple([i, j])
            if not assert_edges_in(edge, edge_list):
                edge_list.append(edge)

    return edge_list


def build_adjacency_random(Node_list, connect_probability):
    '''
    :param Node_list: list type
    :param connect_probability: float number ranges from 0 to 1 inclusive
    :return: list consists adjacency lists
    '''
    Adj = [[] for i in Node_list]
    for node_index,adj_list in enumerate(Adj):
        for i,node in enumerate(Node_list):
            if random.random()<=connect_probability and i != node_index and i not in Adj[node_index] and node_index not in Adj[i]:
                Adj[node_index].append(node)
                Adj[i].append(node_index)

    return Adj


def random_graph_generator(num_nodes, connect_probability = 0.2, random_seed=42):
    random.seed(random_seed)
    Node_list = list(np.arange(num_nodes))
    Adj = build_adjacency_random(Node_list,connect_probability)
    G = nx.Graph()
    G.add_nodes_from(Node_list)
    edge_list = adj_to_edge_list(Adj)
    G.add_edges_from(edge_list)

    return G, Adj

def two_connected_components_example():
    Node_list = list(np.arange(7))
    Adj = [[1],[0,2,4],[1,3],[2],[1],[6],[5]]
    G = nx.Graph()
    G.add_nodes_from(Node_list)
    Edge_list = adj_to_edge_list(Adj)
    G.add_edges_from(Edge_list)

    return G, Adj





if __name__=='__main__':
    G,Adj = random_graph_generator(10)
    print(Adj)
    nx.draw(G,with_labels=True)
    plt.show()
