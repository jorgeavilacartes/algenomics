from typing import Optional
# https://graphviz.readthedocs.io/en/stable/manual.html
from graphviz import Digraph

class PlotDigraph:
    "Plot graph from a set of nodes and a list of edges"
    def __init__(self,):
        # Create an empty graph
        self.new_graph()

    def new_graph(self,):
        "Create an empty graph"
        self.digraph  = Digraph(comment='De Bruijn')
        self.nodes = set()
        self.edges = list()

    def create_dot_graph(self,):
        "Create graph in 'dot' language to be plotted"
        # Add nodes to the graph
        for node in self.nodes: 
            self.add_node(node)
        # Add edges to the graph
        for edge in self.edges: 
            u, v = edge
            self.add_edge(u,v)

    def add_node(self, node: str):
        "Add node with same name"
        self.digraph.node(node, node) 

    def add_edge(self, u, v):
        "Add edge u -> v"
        self.digraph.edge(u,v)

    def show(self,):
        "Print graph"
        self.create_dot_graph()
        return self.digraph

class DeBruijnGraph(PlotDigraph): 
    "Create de Bruijn Graph from a sequence"
    # TODO: create from a list of kmers
    def __init__(self, sequence: Optional[str] = None, kmers: Optional[list] = None, k: int = 3):# Instantiate PlotDigraph attributes
        self.sequence = sequence
        self.kmers = kmers
        self.k  = k
        
        super().__init__() 
        self._build_graph()

    def graph_from_sequence(self,):
        "Given a sequence, create the De Bruijn Graph"
        print("From sequence")
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

    def graph_from_kmers(self,):
        "Given a list of kmers, create the De Bruijn Graph"
        print("From k-mers")
        # Each k-mer is an edge
        for kmer in self.kmers: 
            u,v = kmer[:-1], kmer[1:]
            self.edges.append((u,v))
            self.nodes.add(u)
            self.nodes.add(v)

    def _build_graph(self,): 
        "Build graph from a sequence or a list of kmers"
        if self.sequence is not None:         
            self.graph_from_sequence()
        elif self.kmers is not None: 
            self.graph_from_kmers()