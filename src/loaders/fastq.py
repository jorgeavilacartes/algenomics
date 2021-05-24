# https://github.com/BenLangmead/ads1-notebooks/blob/master/1.04_WorkingWithSequencingReads.ipynb
import json 
from typing import Tuple

from functools import lru_cache

class FastqLoader:
    """Read sequences from a Fastq file"""
    
    def __call__(self,filename: str) -> Tuple[list,list]: 
        "Return sequences and qualities (ASCII-encoded format)"
        self.load(filename)
        return self.sequences, self.qualities

    @lru_cache(maxsize=2)
    def load(self, filename: str):  
        "load sequences and qualities"

        sequences = []
        qualities = []
        with open(filename) as fh:
            while True:
                fh.readline() # skip name line
                seq = fh.readline().rstrip() # read base sequence
                fh.readline() # skip placeholder line
                qual = fh.readline().rstrip() #base quality line
                if len(seq) == 0:
                    break
                sequences.append(seq)
                qualities.append(qual)
        
        self.sequences = sequences
        self.qualities = qualities 
        
    @staticmethod
    def Q_to_phred33(Q: int) -> str:
        "Turn Q into Phred+33 ASCII-encoded quality"
        # HINT:_ 'chr' converts integer to character according to ASCII table
        encoded_quality = chr(Q + 33)
        return encoded_quality
    
    @staticmethod
    def phred33_to_Q(encoded_quality: str) -> int: 
        "Trun Phred+33 ASCII-encoded quality into Q"
        # HINT: 'ord' converts character to integer according to ASCII table
        return ord(encoded_quality) - 33
