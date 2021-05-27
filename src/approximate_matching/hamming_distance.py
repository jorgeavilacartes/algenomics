"""
    For each one-to-one comparison between characters in pattern and the text (T), we have the next operations over the pattern (P),
    based on the difference between P and T (the goal is to fit P to T, with the least possible operations):
    - substitution: the character in the pattern mismatch with the one in T, so it must be replaced in order to match T
    - insertion: there is an extra character in P, and a gap in T (empty space "-" should be added)
    - deletion: correspond to a insertion of an empty space in P in order to fit T

"""

class HammingDistance:

    def __call__(self, t1:str, t2: str): 
        """Given two equal lenght strings, return the hamming distance and a 
        list with indexes for each mismatch"""

        assert len(t1) == len(t2), "Hamming distance is only defined for two equal length strings. Yours are {} and {} characters long.".format(len(t1),len(t2))

        ## Comparison position by position between t1 and t2
        # True: is a mismatch, False: not a mismatch
        mismatches = [not c1 == c2 for c1, c2 in zip(t1,t2)]

        # Get all positions with mismatches
        pos_mismatches = [pos for pos, mismatch in enumerate(mismatches) if mismatch is True]

        # Return the total mistakes 
        return sum(mismatches), pos_mismatches