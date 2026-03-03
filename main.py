from sequence_utils import transcribe, translate

dna = input("Enter DNA sequence: ")

rna = transcribe(dna)
protein = translate(rna)

print("RNA Sequence:", rna)
print("Protein Sequence:", protein)