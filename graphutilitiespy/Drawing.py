import networkx as nx
from scipy.sparse import csr_matrix, csgraph
from graphutilitiespy.Graphs import *

def draw_completesimplegraph(vertices, nodepos, distancetype, writeedgelabels):
    listofverticesandedges = create_completesimplegraph(vertices, nodepos, distancetype)
    print('Drawing a complete simple graph..\n')
    G = nx.Graph()
    G.add_nodes_from(listofverticesandedges[0])
    G.add_weighted_edges_from(listofverticesandedges[1])
    nx.draw_networkx_nodes(G, pos = listofverticesandedges[2])
    nx.draw_networkx_labels(G, pos = listofverticesandedges[2])
    nx.draw_networkx_edges(G, pos = listofverticesandedges[2], edgelist=listofverticesandedges[1], arrows=True, connectionstyle='arc3, rad = 0')
    if writeedgelabels:
        nx.draw_networkx_edge_labels(G, pos = listofverticesandedges[2], edge_labels = nx.get_edge_attributes(G,'weight'), label_pos = 0.6, verticalalignment = 'center')    
    return G

def draw_bipartitesimplegraph(vertices, nodepos, distancetype, sizeoffirstvertexset, writeedgelabels):
    listofverticesandedges = create_bipartitesimplegraph(vertices, nodepos, distancetype, sizeoffirstvertexset)
    print('Drawing a bipartite simple graph..\n')
    G = nx.Graph()
    G.add_nodes_from(listofverticesandedges[0])
    G.add_weighted_edges_from(listofverticesandedges[1])
    nx.draw_networkx_nodes(G, pos = listofverticesandedges[2])
    nx.draw_networkx_labels(G, pos = listofverticesandedges[2])
    nx.draw_networkx_edges(G, pos = listofverticesandedges[2], edgelist=listofverticesandedges[1], arrows=True, connectionstyle='arc3, rad = 0')
    if writeedgelabels:
        nx.draw_networkx_edge_labels(G, pos = listofverticesandedges[2], edge_labels = nx.get_edge_attributes(G,'weight'), label_pos = 0.6, verticalalignment = 'center')    
    return G