class Graph:
    def __init__(self):
        self.edges = []  # список рёбер (edge list)
        self.adjacency_list = {}  # список смежности (adjacency list)

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, start, end, weight):
        self.edges.append((start, end, weight))  # добавление в список рёбер
        if start not in self.adjacency_list:
            self.adjacency_list[start] = []
        self.adjacency_list[start].append((end, weight))

    def remove_edge(self, start, end):
        self.edges = [(s, e, w) for (s, e, w) in self.edges if s != start or e != end]
        if start in self.adjacency_list:
            self.adjacency_list[start] = [(e, w) for (e, w) in self.adjacency_list[start] if e != end]

    def remove_vertex(self, vertex):
        self.edges = [(s, e, w) for (s, e, w) in self.edges if s != vertex and e != vertex]
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
        for connections in self.adjacency_list.values():
            connections[:] = [(e, w) for (e, w) in connections if e != vertex]

    def find_edge(self, start, end):
        return next(((s, e, w) for (s, e, w) in self.edges if s == start and e == end), None)

graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_edge(1, 2, 10)  # добавить ребро с весом 10 между вершинами 1 и 2
print("Edges:", graph.edges)
print("Adjacency List:", graph.adjacency_list)