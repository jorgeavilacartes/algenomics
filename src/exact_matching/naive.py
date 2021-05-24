class Naive:
    "Return a list with indexes where a pattern matches in a sequence"
    
    def __init__(self, sequence: str,): 
        self.sequence = sequence
    
    def __call__(self, pattern: str,):
        matches = self.get_all_match(self.sequence, pattern)
        return True if matches else False, matches
        
    @staticmethod
    def get_all_match(sequence: str, pattern: str): 
        "Get all matches in a sequence for a given pattern"
        matches = []
        p0 = pattern[0]

        max_pos = len(sequence) - len(pattern) + 1
        print("max_pos", max_pos)
        
        # Find match for the first character in pattern
        for i, s in enumerate(sequence): 
            
            # Bound feasible comparison
            if i >= max_pos: break 
                
            # Initialize match as False
            is_match = False
            
            # Find match with first char of the pattern
            if s == p0: 
                
                # Verify if the pattern is contained in the sequence
                for j,p in enumerate(pattern[1:]): 
                    
                    # Break the loop if no-coincidence is found
                    if p != sequence[i+1+j]: 
                        break
                        
                # Otherwise, a match was found
                is_match = True
                
            # Save match
            if is_match: 
                matches.append(i)

        return matches