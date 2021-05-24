# algenomics

# Objetivo
Librería para entender el ADN desde la perspectiva de la biología. 

En esta librería se busca replicar el funcionamiento biológico mediante herramientas computacionales. Construyendo cada elemento básico y sus acciones de la manera más fidedigna posible.

Esta librería NO tiene por objetivo estar optimizada para abordar problemas de alta complejidad y requerimientos computacionales. Su objetivo es ser una herramienta que conecte los conocimientos biológicos de manera natural con la programación. Para cumplir con este objetivo, se han implementado clases relativas al ADN (`DNA`), proteínas (`RNApolymerase` encargada de la transcripción de ADN)


# Ejemplos de uso.

Para pasar de un gen a una proteína, primero hay que generar una secuencia de nucleótidos. Esta tarea, llamada `transcripción` la realiza la proteína ARN polimerasa.


```python
from algenomics import (
    DNA,
    RNApolymerase,
)

dna = DNA("AATTCCGC")

# output 
> print(dna)
> 'C': 3; 'A': 2; 'T': 2; 'G': 1
> 'length': 8
> DNA('AATTCCGC')

# 
dna.reverse_complement()
> 'GCGGAATT'
```

# Loaders
```python
from algenomics import (
    FastqLoader,
    FastaLoader,
)
```

Inspirado en el libro "¿Qué puede salir mal?" de "La Hiperactina".

Otras características están relacionadas a bioinformática, desde la perspectiva de grafos. 

Próximamente:

- De Bruijn Graph