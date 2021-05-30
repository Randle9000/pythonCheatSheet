# example of graph
dict_graph = {'a': ['c'],
              'b': ['c', 'e'],
              'c': ['a', 'b', 'd', 'e'],
              'd': ['c'],
              'e': ['b', 'c']}


def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node,neighbour))
    return edges

dict_edges = generate_edges(dict_graph)
print(dict_edges, len(dict_edges))