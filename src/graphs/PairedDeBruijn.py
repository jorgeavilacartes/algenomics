from typing import Optional
from .plot import PlotDigraph

class PairedDeBruijnGraph(PlotDigraph):
    "Create de Bruijn Graph from a self.sequence"
    def __init__(self, 
                    sequence: Optional[str] = None,
                    kmers: Optional[list] = None,
                    k: int = 3, # k-mer
                    d: int = 1, # distance between pairs of k-mers
                    ):# Instantiate PlotDigraph attributes
        self.sequence = sequence
        self.kmers = kmers
        self.k  = k
        self.d  = d 

        super().__init__() 
        self._build_graph()

    def graph_from_sequence(self,):
        "Given a self.sequence, create the Paired De Bruijn Graph"
        print("From self.sequence")

        # for j,c in enumerate(self.self.sequence):
        #     if j+self.d +self.k-1  < len(self.self.sequence):
        #         # Nodes: each (k-1)-mer is a node
        #         # first kmer
        #         u1 = self.self.sequence[j   : j+self.k]
        #         v1 = self.self.sequence[j+1 : j+self.k+1]
                
        #         # second kmer, separated d-spaces from first kmer
        #         u2 = self.self.sequence[j+self.d   :j+self.k+self.d]
        #         v2 = self.self.sequence[j+self.d+1 :j+self.k+self.d]
                
        #         if len(u1) == len(u2) == len(v1) == len(v2) == self.k-1:
        #             # Add Edge
        #             u = u1 + "\n" + u2
        #             v = v1 + "\n" + v2

        #             self.edges.append((u,v))
                    
        #             # Add Nodes
        #             self.nodes.add(u)
        #             self.nodes.add(v)

        d = self.d
        k = self.k

        for j,c in enumerate(self.sequence):
            
            #Nodes
            if j + d +k   < len(self.sequence):
                # Nodes: each (k-1)-mer is a node
                # first kmer
                u1 = self.sequence[j   : j+k]
                u2 = self.sequence[j+d : j+k+d]
                
                # second kmer, separated d-spaces from first kmer
                v1 = self.sequence[j+1   : j+k+1]
                v2 = self.sequence[j+d+1 :j+k+d+1]
                
                # Add Nodes
                u = u1 + "\n" + u2
                v = v1 + "\n" + v2

                self.nodes.add(u)
                self.nodes.add(v)

                # Add Edge
                self.edges.append((u,v))

    def graph_from_kmers(self,):
        "Given a list of kmers, create the Paired De Bruijn Graph"
        print("From k-mers")
        # # Each k-mer is an edge
        # for kmer in self.kmers: 
        #     u,v = kmer[:-1], kmer[1:]
        #     self.edges.append((u,v))
        #     self.nodes.add(u)
        #     self.nodes.add(v)
        pass 

    def _build_graph(self,): 
        "Build graph from a self.sequence or a list of kmers"
        if self.sequence is not None:         
            self.graph_from_sequence()
        elif self.kmers is not None: 
            self.graph_from_kmers()