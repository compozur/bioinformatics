from collections import defaultdict

def nucleotide_counts(dna_string):
    counts = defaultdict(int)
    for nuc in dna_string:
        counts[nuc] += 1
    return counts

dna_string = "AAAAAACAGCGAGTCGGCACGTCCAGTGCAGGCGCCCGGCACATTGAGTCTAGCGAAGAGTCTTT"
counts = nucleotide_counts(dna_string)
print(counts)
