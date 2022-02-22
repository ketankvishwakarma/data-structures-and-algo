
class Graph:

    def __init__(self) -> None:
        self.adjacency_list = {}
    
    def __str__(self) -> str:
        return "{}".format(self.adjacency_list)

    def add_vertex(self,vertex) -> bool:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edgd(self, vertex1,vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self,vertex1,vertex2):
        self.adjacency_list[vertex1] = list(filter(lambda v: v!=vertex2,self.adjacency_list[vertex1]))
        self.adjacency_list[vertex2] = list(filter(lambda v: v!=vertex1,self.adjacency_list[vertex1]))

    def remove_vertex(self,vertex):
        
g = Graph()

g.add_vertex("Dalas")
g.add_vertex("Tokio")
g.add_vertex("Aspin")
print(g)

g.add_edgd("Dalas","Tokio")
print(g)

g.remove_edge("Dalas","Tokio")
print(g)