# Nucleotidos complementarios para pasar de ADN a ARN
DNA2RNA = {
    "A": "U",
    "T": "A",
    "C": "G",
    "G": "G"
}

class RNApolymerase:
    "Protein in charge to make transcription from DNA to RNA"

    @staticmethod
    def transcription(sequence: str): 
        "Get RNA from DNA"
        rna = (DNA2RNA.get(nucleotide) for nucleotide in sequence)
        return "".join(rna)

    @staticmethod
    def about_me():
        """
        (...) Para pasar de un gen a una proteína, primero hay que generar una secuencia de nucleótidos. 
        Esta tarea, llamada transcripción la realiza la proteína ARN polimerasa.
        """