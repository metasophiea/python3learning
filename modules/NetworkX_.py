import networkx, matplotlib

graph = networkx.Graph()

# Adding nodes
graph.add_node("a")
graph.add_node(1)
graph.add_nodes_from(["1","2","3"])

# Adding connections
graph.add_edge(1,2) # 1 exists in the graph, but 2 doesn't. This node will be added automatically
graph.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

# Print Graph
networkx.draw( graph ) # requires the module "matplotlib"
matplotlib.pyplot.show() # display

print("Nodes of graph:",graph.nodes())
print("Edges of graph:",graph.edges())