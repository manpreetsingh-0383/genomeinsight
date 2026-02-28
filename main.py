# Import GC content function
from gc_content import calculate_gc_content

# Take DNA sequence input
dna_sequence = input("Enter a DNA sequence: ")

# Convert sequence to uppercase
dna_sequence = dna_sequence.upper()

# Calculate sequence length
sequence_length = len(dna_sequence)

# Count G and C
g_count = dna_sequence.count("G")
c_count = dna_sequence.count("C")

# Calculate GC content using function
gc = calculate_gc_content(dna_sequence)

# Display results
print("\n--- GenomeInsight Analysis ---")
print("Sequence Length:", sequence_length)
print("G count:", g_count)
print("C count:", c_count)
print("GC Content:", gc, "%")