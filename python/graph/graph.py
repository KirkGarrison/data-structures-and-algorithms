class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def size(self):
        return len(self.adjacency_list)

    def get_nodes(self):
        return list(self.adjacency_list.keys())

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if not end_vertex in self.adjacency_list:
            raise KeyError()
        edge = Edge(end_vertex, weight)
        self.adjacency_list[start_vertex].append(edge)

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def breadth_first(self, vertex):

        explored = {}
        level = {}
        parent = {}
        output = []
        list = []

        for node in self.adjacency_list.keys():
            explored[node] = False
            parent[node] = None
            level[node] = -1

        source_node = 'A'
        explored[source_node] = True
        level[source_node] = 0
        list.put(source_node)

        while not list.empty():
            get = list.get()
            output.append(get)

        for v in self.adjacency_list[get]:
            if not explored[v]:
                explored[v] = True
                parent[v] = get
                level[v] = level[get]+1
                list.put(v)

        return output

class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Vertex:

    def __init__(self, value):
        self.value = value
