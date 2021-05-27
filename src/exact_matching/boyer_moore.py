class BoyerMoore:

    def __init__(self, pattern: str, alphabet: str):
        
        self.pattern  = pattern 
        self.alphabet = alphabet
        
        # Generate preprocessing table for alphabet (rows) and pattern (columns)
        self.preprocessing()
        
    def __call__(self,):
        "Find matches with Boyer-Moore algorithm"
        pass 

    def preprocessing(self,): 
        "Generate preprocessing table for alphabet (rows) and pattern (columns)"
        pass
    