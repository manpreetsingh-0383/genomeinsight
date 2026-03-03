# Transcription: DNA → RNA
def transcribe(dna):
    dna = dna.upper()
    return dna.replace("T", "U")
# Full Translation: RNA → Protein with proper ORF detection
def translate(rna):
    genetic_code = {
        # Phenylalanine
        "UUU": "F", "UUC": "F",
        # Leucine
        "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        # Isoleucine
        "AUU": "I", "AUC": "I", "AUA": "I",
        # Methionine (Start)
        "AUG": "M",
        # Valine
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        # Serine
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
        # Proline
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        # Threonine
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        # Alanine
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        # Tyrosine
        "UAU": "Y", "UAC": "Y",
        # Histidine
        "CAU": "H", "CAC": "H",
        # Glutamine
        "CAA": "Q", "CAG": "Q",
        # Asparagine
        "AAU": "N", "AAC": "N",
        # Lysine
        "AAA": "K", "AAG": "K",
        # Aspartic Acid
        "GAU": "D", "GAC": "D",
        # Glutamic Acid
        "GAA": "E", "GAG": "E",
        # Cysteine
        "UGU": "C", "UGC": "C",
        # Tryptophan
        "UGG": "W",
        # Arginine
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
        # Glycine
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
        # Stop Codons
        "UAA": "Stop", "UAG": "Stop", "UGA": "Stop"
    }

    rna = rna.upper()

    # Validate RNA sequence
    for base in rna:
        if base not in "AUCG":
            return "Invalid RNA sequence."

    protein = ""
    start_found = False

    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]

        # Wait until start codon
        if not start_found:
            if codon == "AUG":
                start_found = True
                protein += "M"
            continue

        # After start codon
        if genetic_code[codon] == "Stop":
            break

        protein += genetic_code[codon]

    if not start_found:
        return "No start codon found."

    return protein