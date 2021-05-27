import numpy as np
from collections import OrderedDict, namedtuple

class Naive:
    """Naive approach for 'Edit Distance' (recursive function).
    The goal is to turn t1 -> t2 with the minimum number of 'edits'.
    Allowed 'edits' are:
    - 'substitution'  of an element in t1
    - 'insertion' of an element in t1
    - 'deletion' deletion of an element in t1
    """
    # copy from https://www.youtube.com/watch?v=8Q2IEIY2pDU&list=PL2mpR0RYFQsBiCWVJSvVAO3OJ2t7DzoHA&index=33

    Edit = namedtuple('Edit',['kind', 'argmin', 'index'])    
    
    def __init__(self,):
        self.edits  = [] # to save all calls
        self.ops    = []   # all operations with index, argmin and kind of edit
        self.len_T  = 0  # initialize as 0 to get new input strings
        self.initial_t1 = str()
        self.current_t1 = str()

    def __call__(self, t1: str, t2: str):
        """A recursive function to calculate edit distance: 
        This will calculate the minimum amount of edits to transform t1 into t2
        """
        # # --------
        # # FIXME: tracking edits, is this useful?
        # # With this we can notice if a new string want to be compared
        # # len of t1 is always decreasing in a next call
        # if len(t1) > self.len_T:
        #     print("Inicio nuevo T")
        #     self.len_T = len(t1)        # lenght of the initial t1 that will forced to fit t2
        #     self.initial_t1 = t1

        # # If the current t1 has changed, get 
        # self.current_t1 = self.current_t1 if t1 == self.current_t1 else t1
        # # -------

        if len(t1) == 0:
            return len(t2)
        if len(t2) == 0:
            return len(t1)

        # Calculation for each kind of edits
        prefix_t1, x = t1[:-1], t1[-1]
        prefix_t2, y = t2[:-1], t2[-1] 
        delta = self.delta(x,y) # 1 if x!=y, 0 otherwise
        
        # Three options to edit the string usign prefixes
        edits = OrderedDict(
            substitution = self.__call__(prefix_t1, prefix_t2) + delta, # substite 'x' by 'y' if delta = 0
            deletion     = self.__call__(prefix_t1, t2)      + 1,       # delete         
            insertion    = self.__call__(t1, prefix_t2)      + 1                 
        )
        
        index = len(prefix_t1) #self.len_T - len(t1) # index where the 'edit' will occur

        # Get kind of edit
        argmin      = int(np.argmin(np.array(list(edits.values()))))
        kind_edit   = list(edits.keys())[argmin]        

        # # If an edit must be done, then, save the info
        # # -----
        # # FIXME: Tracking edits is not working
        # if delta == 1: 
        #     self.edits.append(edits)
        #     self.ops.append(self.Edit(kind_edit,argmin, index))
        # elif delta == 0 and kind_edit == 'substitution': 
        #     self.ops.append(self.Edit('nothing',argmin, index))
        # # ----

        return edits[kind_edit]

    @staticmethod
    def delta(c1,c2): 
        return 1 if c1 != c2 else 0

    def track_edits(self,):
        pass

class DynamicProgramming: 
    "Edit distance using dynamic programming"
    
    def __call__(self, t1:str, t2:str): 
        
        # Matrix of distance,  t1:rows, t2:columns (first col and row is empty char)
        dims_D = (len(t1)+1, len(t2)+1)
        D = np.zeros(dims_D) # dims = len(t1)+1 , len(t2)+1
        
        # First row and fisrt column incremental for 0...lenght-1
        D[:,0] = range(len(t1)+1) # first column
        D[0,:] = range(len(t2)+1) # first row

        for row in range(1,len(t1)+1):
            for col in range(1,len(t2)+1): 
                dist_hor = D[row,col-1] + 1 
                dist_ver = D[row-1,col] + 1 
                dist_diag = D[row-1,col-1] + self.delta(t1[row-1], t2[col-1])
                
                # Compute and update edit distance for the current position
                D[row,col] = min(dist_hor, dist_ver, dist_diag)
        
        return int(D[-1,-1])

    @staticmethod
    def delta(c1,c2): 
        return 1 if c1 != c2 else 0