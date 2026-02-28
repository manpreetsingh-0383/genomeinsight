# Function to calculate GC content of a DNA sequence

def calculate_gc_content(sequence):

    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_content = ((g_count + c_count) / len(sequence)) * 100

    return gc_content