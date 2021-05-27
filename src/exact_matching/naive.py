class Naive:
    "Return a list with indexes where a pattern matches in a sequence"
    
    def __call__(self, pattern: str, sequence: str):
        matches = self.get_all_match(pattern, sequence)
        return matches
        
    
    def get_all_match(self, pattern: str, sequence: str,): 
        "Get all matches in a sequence for a given pattern"
        matches = []
        p0 = pattern[0]

        max_pos = len(sequence) - len(pattern) + 1
        
        # Find match for the first character in pattern
        for i, s in enumerate(sequence): 
            
            # Bound feasible comparison
            if i >= max_pos: break 
                
            # Initialize match as False
            is_match = False
            
            # Find match with first char of the pattern
            if s == p0: 
                # # Verify if the rest of the pattern is contained in the sequence
                is_match = self.pattern_is_match(pattern, sequence[i:])
                
            # Save match
            if is_match: 
                matches.append(i)

        return matches
        

    @staticmethod
    def pattern_is_match(pattern, sequence):
        "Verify if pattern[1:] match with the prefix of sequence[1:]"
        # Verify if the pattern is contained in the sequence
        for j,p in enumerate(pattern[1:]): 
            
            # Break the loop if no-coincidence is found
            if p != sequence[j+1]: 
                return False

        return True