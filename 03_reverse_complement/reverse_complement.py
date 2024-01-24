def reverse_complement(dna_sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complement[nucleotide] for nucleotide in dna_sequence])[::-1]

dna_seq = "AGAGATTCGTTACTAC"

rev_comp = reverse_complement(dna_seq)
print(f"Reverse Complement: {rev_comp}")

