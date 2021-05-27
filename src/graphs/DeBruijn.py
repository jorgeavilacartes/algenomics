# https://graphviz.readthedocs.io/en/stable/manual.html
from graphviz import Digraph

class PlotDigraph:
    "Plot graph from a set of nodes and a list of edges"
    def __init__(self, ):
        self.digraph  = Digraph(comment='De Bruijn')
        self.nodes = set()
        self.edges = list()

    def create_dot_graph(self,):
        for node in self.nodes: 
            self.add_node(node)

        for edge in self.edges: 
            u, v = edge
            self.add_edge(u,v)

    def add_node(self, node: str):
        self.digraph.node(node, node) 

    def add_edge(self, u, v):
        "Add edge u -> v"
        self.digraph.edge(u,v)

    def show(self,):
        "Print graph"
        self.create_dot_graph()
        return self.digraph

class DeBruijnGraph(PlotDigraph): 
    "Create de Bruijn Graph"
    def __init__(self, sequence: str, k: int = 3):
        super().__init__()
        self.sequence = sequence
        self.k  = k
        self.create_graph()

    def create_graph(self,):
        
        for j,c in enumerate(self.sequence):
            if j+self.k-1 < len(self.sequence):
                # Nodes: each (k-1)-mer is a node
                u = self.sequence[j:j+self.k-1] 
                v = self.sequence[j+1:j+self.k]
                
                # Add Edge
                self.edges.append((u,v))
                
                # Add Nodes
                self.nodes.add(u)
                self.nodes.add(v)