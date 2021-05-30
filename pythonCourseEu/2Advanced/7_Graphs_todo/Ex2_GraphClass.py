class Graph:

    def __init__(self, graph_dict=None):
        """
        Initialize the graph object
        if no dict or None is given then created empty dict
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """
        return the list of vertices
        """
        return list(self.__graph_dict.keys())


    def edges(self):
        """"
        return the list of all edges
        """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """
        add vertex to existing graph
        """
        if vertex not in self.__graph_dict.keys():
            self.__graph_dict[vertex] = []

    def add_edges(self, edge):
        """
        add edge the communication between vertices
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if (neighbour, vertex) not in edges:
                    edges.append((vertex, neighbour))
        return edges

if __name__ == "__main__":
    dict_graph = {'a': ['d'],
                  'b': ['c'],
                  'c': ['b', 'c', 'd', 'e'],
                  'd': ['a', 'c'],
                  'e': ['c'],
                  'f': []}

    graph = Graph(dict_graph)
    print('vertices', graph.vertices())
    print('edges', graph.edges())



