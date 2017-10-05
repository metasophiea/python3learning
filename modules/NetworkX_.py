import networkx, matplotlib

"""
# Graphing Example One - Simple
graph = networkx.Graph()

# Adding nodes
graph.add_node("a")
graph.add_node(1)
graph.add_nodes_from(["1","2","3"])

# Adding connections
graph.add_edge(1,2) # 1 exists in the graph, but 2 doesn't. This node will be added automatically
graph.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

# Print Graph
networkx.draw( graph,with_labels=True ) # requires the module "matplotlib"
matplotlib.pyplot.show() # display

print("Nodes of graph:",graph.nodes())
print("Edges of graph:",graph.edges())
"""

"""
# Graphing Example Two - Generating a Path Graph
graph = networkx.path_graph(4) # generating the simple path graph of nodes labeled by their number

networkx.draw(graph,with_labels=True)
matplotlib.pyplot.show()
print("Nodes of graph:",graph.nodes())
print("Edges of graph:",graph.edges())
"""

# Graphing Example Three - Renaming Nodes
graph = networkx.path_graph(5) # generating the simple path graph of nodes labeled by their number
cities = {
    0:"Toronto",
    1:"London",
    2:"Berlin",
    3:"New York"
    } # creation of a new dictionary, where the node labels are keys to the new labels

newGraph = networkx.relabel_nodes(graph,cities,copy=True) # this leaves the original graph alone (default is true)
# interestingly, this command can take a method in where 'cities' went, which would take one argument to edit the lables itself
 
networkx.draw(graph,with_labels=True)
matplotlib.pyplot.savefig("path_graph_cities.png")
matplotlib.pyplot.show()
networkx.draw(newGraph,with_labels=True)
matplotlib.pyplot.savefig("path_graph_cities.png")
matplotlib.pyplot.show()

print("Nodes of graph:",newGraph.nodes())
print("Edges of graph:",newGraph.edges())


