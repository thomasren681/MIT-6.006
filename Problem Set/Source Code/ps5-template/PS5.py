import networkx as nx
from UndGraphGenerator import adj_to_edge_list
import numpy as np
import matplotlib.pyplot as plt
from BFS import *
from DFS import *


#######PS 5-1-a#######
# Adj = [[2],[3,4,5],[1,3,4],[1,2],[1,2,5],[1,4]]
# Edge_list = adj_to_edge_list(Adj)
#
# G = nx.Graph()
# Node_list = list(np.arange(6))
# G.add_nodes_from(Node_list)
# G.add_edges_from(Edge_list)
# nx.draw(G,with_labels=True)
# plt.show()

#######PS 5-1-b#######
Adj = {'A':['B'],
       'B':['C','D'],
       'C':['E','F'],
       'D':['E','F'],
       'E':None,
       'F':['D','E']}

#######PS 5-1-c#######
