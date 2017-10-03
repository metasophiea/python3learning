#   The classic world of graph theory. Graphs are data structures consisting of nodes and connections (or 'vertexes' and 'edges')
# Each node can have any number of connections to any other node (even multiple connections to the same one). There are two types
# of graph; 'directed' and 'undirected', which simply refer to the nature of a connection (whether they have a direction or not)
# connections in a 'directed' graph are called 'arcs'.
#
#   A node's 'degree' refers to how many connections it has, with an "isolated vertice" having no connections. Collecting the
# degrees of all the nodes and placing them in decending order produces the "Degree Sequence". Interestingly, Isomorphic graphs
# have the same degree sequence (though the reverse is not necessarily true)(Isomorphic graphs are ones which have the same number
# of nodes and the same connections between those nodes, but aren't displayed in the same pattern)
#   The Erdös-Gallai theorem is used to determin if a degree sequence has a corresponding "simple graph". A 'simple graph' is an
# undirected graph in which identical connections and self connections are not allowed.
#
#   A graph's density relates to how many connections is has verses how many it could have (I think, in a 'simple graph' situation)
# One divides the current number over the maximum number to produce a number between 0 and 1. 0 graphs are called "isolated" graphs,
# graphs with low values are called "sparse", higher is "dense" and ones with maximum connections are called "complete".
#
#   A "connected" graph, is one where a path can be produced between any two nodes. 
#
#   The "distance" between any two nodes, is calculated as the route with the fewest hops. Node "eccentricity" is defined as the longest
# possible distance to a node from that node in the graph, produced by taking the shortest distance between a root node and all other
# nodes in the graph, finding the longest. A graphs "diameter" is the biggest 'eccentricity' out of all the nodes.
#
#
# Tree/Forest
#       A 'Tree' is a connected collection of nodes in an undirected graph; as such, there could be more than one tree in a graph
#   if the connected collections of nodes are multiple distinct networks. A 'tree' is a connected network of 1 or more nodes, A 
#   graph of 1 or  more 'trees' is called a forest. In a tree there are no cycles, thus any two nodes of the tree are connected 
#   by one simple path.
#       A Spanning Tree is a subset of a regular graph which contains all the nodes, but only the connections needed to create
#   a tree. As such, there are sometimes a multiple valid spanning trees for a given graph.
#
# Hamiltonian Path
#       This is a path in an undirected or directed graph that visits each node exactly once. A Hamiltonian Cycle (or circuit)
#   is a path who's end connects to its start. 
#

#   The simplist way to represent a graph (in python anyway) is as follows:
#   {
#       "nodeName":["nodeName","nodeName"],
#       "nodeName":["nodeName","nodeName"],
#   }
#       where each key refers to a node, and the attached list of node names, the nodes to which it is connected. Obviously, it
# would be nicer to bundle this structure into a class with handy methods to go along with it:
# (running this file tests the 'Graph' class)
#
# The class' structure is as follows:
#   className: Graph
#       variables:
#           __graph_dict            - where the graph is actually stored
#       methods:
#           __init__                - constructor, is capable of importing a (correctly) pre-formed graph
#           __generate_edges        - goes through the graph to produce a list of sets. ( {"sourceNode","destinationNode"} )
#           __str__                 - returns a string-ified representation of the data
#           vertices                - returns the nodes of the graph
#           edges                   - returns the connections of the graph, as a list of sets. ( {"sourceNode","destinationNode"} )
#           add_vertex              - adds the supplied name as a node of the graph (unless it's already there)
#           add_edge                - takes a set of two node names, and adjusts the graph appropriately
#           find_path               - takes two points and attempts to find a path between them
#           find_path               - takes two points and attempts to find all the paths between them
#           vertex_degree           - counts the number of connections a node has (self connections are counted twice (once per literal connection))
#           find_isolated_vertices  - returns a list of nodes without connections
#           delta                   - returns the minimum degree found within the graph
#           Delta                   - returns the maximum degree found within the graph
#           degree_sequence         - returns the degree sequence (an array of each node's degree in decending order)
#  static:  erdoes_gallai           - Tests to see if the sequence fufills the Erdös-Gallai theorem

# The class' graph is implemented like a 'directed' graph, but has enough connections to look like a 'undirected' graph. Some of the methods
# take advantage of this fact













class Graph(object):

    def __init__(self, graph_dict=None):
        # initializes a graph object If no dictionary or None is given, an empty dictionary will be used
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def __generate_edges(self):
        # A method generating the edges of the graph "graph". Edges are represented as sets with one (a loop back to the vertex) or two vertices 
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def vertices(self):
        # returns the vertices of a graph
        return list(self.__graph_dict.keys())

    def edges(self):
        # returns the edges of a graph
        return self.__generate_edges()

    def add_vertex(self, vertex):
        # If the vertex "vertex" is not in self.__graph_dict, a key "vertex" with an empty list as a value is added to the dictionary. Otherwise nothing has to be done. 
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        # assumes that edge is of type set, tuple or list; between two vertices can be multiple edges!
        (vertex1, vertex2) = tuple(set(edge))
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def find_path(self, start_vertex, end_vertex, path=None):
        # find a path from start_vertex to end_vertex in graph
        #   At its core, this function goes through every possible route to find one that works.

        # It starts with some checks to make sure the 'path' variable is at least an empty array,
        # loads in the '__graph_dict' and places the 'start_vertex' variable on the end of the
        # 'path' variable. It then checks to see if the 'start_vertex' happens to be the 'end_vertex'
        # or if the 'start_vertex' variable is in the graph at all.
        if path == None: path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex: return path
        if start_vertex not in graph:  return None

        #   This is where the magic happens; for each node that is connected to the node 'start_vertex'
        # and that isn't already in the path; the method calls itself with the node, end node and the 
        # current path. The recursion will continue going through all routes until the 'start_vertex' is
        # the same as the 'end_vertex'; at which point it will start returning the path. If any of the
        # method instances start returning, it means that a route has been found and the top level method
        # will complete.
        #   A method instance that has no-where left to go will return an empty list, which proves 'false'
        # in the 'extended_path' test, pushing the loop onto the next iteration.
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path: 
                    return extended_path
                
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        # find all paths from start_vertex to end_vertex in graph

        #   This method works in the same way as 'find_path', except that the method will always return
        # an list of lists. As such, the recursive return value is appended to a 'paths' variable (instead
        # of the 'extended_path' test)

        graph = self.__graph_dict 
        path = path + [start_vertex]

        if start_vertex == end_vertex: return [path]
        if start_vertex not in graph: return []

        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path)
                for p in extended_paths: 
                    paths.append(p)

        return paths
    
    def vertex_degree(self, vertex):
        """ The degree of a vertex is the number of edges connecting
            it, i.e. the number of adjacent vertices. Loops are counted 
            double, i.e. every occurence of vertex in the list 
            of adjacent vertices. """ 
        adj_vertices = self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex) # counts the number of connections leaving the vertex, plus adds connections that connect back to the vertex
        return degree

    def find_isolated_vertices(self):
        """ returns a list of isolated vertices. """

        # This one simply goes through each node to discover which have no connections
        graph = self.__graph_dict
        isolated = []
        for vertex in graph:
            if not graph[vertex]:
                isolated += [vertex]
        return isolated

    def delta(self):
        """ the minimum degree of the vertices """
        min = 100000000
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree < min:
                min = vertex_degree
        return min
        
    def Delta(self):
        """ the maximum degree of the vertices """
        max = 0
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > max:
                max = vertex_degree
        return max

    def degree_sequence(self):
        """ calculates the degree sequence """
        seq = []
        for vertex in self.__graph_dict:
            seq.append(self.vertex_degree(vertex))
        seq.sort(reverse=True)
        return tuple(seq)

    @staticmethod
    def erdoes_gallai(dsequence):
        """ Checks if the condition of the Erdoes-Gallai inequality 
            is fullfilled 
            dsequence has to be a valid degree sequence
        """
        if sum(dsequence) % 2:
            # sum of sequence is odd
            return False
        for k in range(1,len(dsequence) + 1):
            left = sum(dsequence[:k])
            right =  k * (k-1) + sum([min(x,k) for x in dsequence[k:]])
            if left > right:
                return False
        return True

    def density(self):
        """ method to calculate the density of a graph """
        g = self.__graph_dict
        V = len(g.keys())
        E = len(self.edges())
        return 2.0 * E / (V *(V - 1))

    def is_connected(self, vertices_encountered=None, start_vertex=None):
        """ determines if the graph is connected """
        # This is done by selected a root node at random, then propagating out through all the
        # nodes its connected to, and all the nodes they are connected to (etc.) while populating
        # a set of all nodes encountered. When all nodes in this propagating have been encountered,
        # the set is compared to the total graph; if both have the same set of nodes; the graph
        # is connected.

        #   Set-up procedures 
        # (making sure 'vertices_encountered' is a set, gathering the graph and its keys, 
        # making sure 'start_vertex' has a node value before it's added to the 'vertices_encountered' set)
        if vertices_encountered is None: vertices_encountered = set()
        gdict = self.__graph_dict; vertices = list(gdict.keys())
        if not start_vertex: start_vertex = vertices[0] # chosse a vertex from graph as a starting point  
        vertices_encountered.add(start_vertex)

        #   Recursive functionality
        if len(vertices_encountered) == len(vertices): return True      # is the encountered set of equal length to the graph's list of nodes? if so return True, otherwise..   
        else:                                                           #
            for vertex in gdict[start_vertex]:                          #   for each node connected to 'start_vertex'
                if vertex not in vertices_encountered:                  #       if the node is not in the encountered set, call the function again with this node as the 'start_vertex'
                    if self.is_connected(vertices_encountered, vertex): #
                        return True                                     #           if that returned true, return true, otherwise continue on the for loop

        return False

    def diameter(self):
        """ calculates the diameter of the graph """
        
        # collect all the nodes and create a unique list of pairs
        v = self.vertices() 
        pairs = [ (v[i],v[j]) for i in range(len(v)-1) for j in range(i+1, len(v))]

        # for each pair; find all the paths between them, and store the shortest in the 'smallest_paths' list
        smallest_paths = []
        for (s,e) in pairs:
            paths = self.find_all_paths(s,e)
            smallest = sorted(paths, key=len)[0]
            smallest_paths.append(smallest)
        smallest_paths.sort(key=len)        # sort this list by list length
        return len(smallest_paths[-1]) - 1  # logically, the longest route is now at the end of this list









if __name__ == "__main__":
    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }

    graph = Graph(g)

    # print("Vertices of graph:")
    # print(graph.vertices())
    # print()

    # print("Edges of graph:")
    # print(graph.edges())
    # print()

    # print("Add vertex:")
    # graph.add_vertex("z")
    # print("Vertex \"z\" added")
    # print()

    # print("Vertices of graph:")
    # print(graph.vertices())
    # print()
 
    # print("Add an edge:")
    # graph.add_edge({"a","z"})
    # print("Edge {\"a\",\"z\"} added")
    # print()
    
    # print("Vertices of graph:")
    # print(graph.vertices())
    # print()

    # print("Edges of graph:")
    # print(graph.edges())
    # print()

    # print('Adding an edge {"x","y"} with new vertices:')
    # graph.add_edge({"x","y"})
    # print("Vertices of graph:")
    # print(graph.vertices())
    # print("Edges of graph:")
    # print(graph.edges())
    # print()

    # print('The path from vertex "a" to vertex "b":')
    # path = graph.find_path("a", "b")
    # print(path)
    # print()

    # print('The path from vertex "a" to vertex "f":')
    # path = graph.find_path("a", "f")
    # print(path)
    # print()

    # print('The path from vertex "c" to vertex "c":')
    # path = graph.find_path("c", "c")
    # print(path)
    # print()


    # g = {   "a" : ["d", "f"],
    #         "b" : ["c"],
    #         "c" : ["b", "c", "d", "e"],
    #         "d" : ["a", "c"],
    #         "e" : ["c"],
    #         "f" : ["d"]
    # }
    # graph = Graph(g)

    # print('All paths from vertex "a" to vertex "b":')
    # path = graph.find_all_paths("a", "b")
    # print(path)
    # print()

    # print('All paths from vertex "a" to vertex "f":')
    # path = graph.find_all_paths("a", "f")
    # print(path)
    # print()

    # print('All paths from vertex "c" to vertex "c":')
    # path = graph.find_all_paths("c", "c")
    # print(path)
    # print()

    # print("How many connections does node C have?")
    # print( graph.vertex_degree("c") )
    # print()

    # print("Which nodes have no connections?")
    # print( graph.find_isolated_vertices() )
    # print()

    # print("What are the minimum and maximum degrees in this graph?")
    # print( "Min" + str(graph.delta()) )
    # print( "Max" + str(graph.Delta()) )
    # print()

    # print("Graph's degree sequence: " + str( graph.degree_sequence() ) )
    # print()

    # print("Does the degree sequence (5, 2, 1, 1, 1, 0) satisfy the Erdoes-Gallai therom?")
    # print( Graph.erdoes_gallai( (5, 2, 1, 1, 1, 0) ) )
    # print()

# Graph Density
    # g = { "a" : ["d","f"],
    #     "b" : ["c","b"],
    #     "c" : ["b", "c", "d", "e"],
    #     "d" : ["a", "c"],
    #     "e" : ["c"],
    #     "f" : ["a"]
    # }
    # complete_graph = { 
    #     "a" : ["b","c"],
    #     "b" : ["a","c"],
    #     "c" : ["a","b"]
    # }
    # isolated_graph = { 
    #     "a" : [],
    #     "b" : [],
    #     "c" : []
    # }

    # print( "Graph density: " + str(graph.density()) )
    # print( "Graph density: " + str(Graph(g).density()) )
    # print( "Graph density (complete graph): " + str(Graph(complete_graph).density()) )
    # print( "Graph density (isolated graph): " + str(Graph(isolated_graph).density()) )
    # print()

# Connected Graphs
    # g = { "a" : ["d"],
    #       "b" : ["c"],
    #       "c" : ["b", "c", "d", "e"],
    #       "d" : ["a", "c"],
    #       "e" : ["c"],
    #       "f" : []
    # }

    # g2 = { "a" : ["d","f"],
    #        "b" : ["c"],
    #        "c" : ["b", "c", "d", "e"],
    #        "d" : ["a", "c"],
    #        "e" : ["c"],
    #        "f" : ["a"]
    # }

    # g3 = { "a" : ["d","f"],
    #        "b" : ["c","b"],
    #        "c" : ["b", "c", "d", "e"],
    #        "d" : ["a", "c"],
    #        "e" : ["c"],
    #        "f" : ["a"]
    # }


    # graph = Graph(g)
    # print(graph)
    # print(graph.is_connected())

    # graph = Graph(g2)
    # print(graph)
    # print(graph.is_connected())

    # graph = Graph(g3)
    # print(graph)
    # print(graph.is_connected())
    # print()

# Graph Distance and Diameter
    g = { "a" : ["c"],
          "b" : ["c","e","f"],
          "c" : ["a","b","d","e"],
          "d" : ["c"],
          "e" : ["b","c","f"],
          "f" : ["b","e"]
    }

    print( Graph(g).diameter() )
    # ans: 3 as  a -> c -> e -> f