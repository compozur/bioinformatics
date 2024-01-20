from collections import defaultdict

def most_frequent_kmers(sequence, k_len):
    kmer_freq = defaultdict(int)

    for i in range(len(sequence)-k_len+1):
        kmer = sequence[i:i+k_len]
        kmer_freq[kmer] += 1

    max_freq = max(kmer_freq.values())
    max_kmers = [kmer for kmer, freq in kmer_freq.items() if freq == max_freq]

    return max_freq, max_kmers

dna_seq = "AGAGATTCGTTACTAC"
k_len = 3
max_freq, max_kmers = most_frequent_kmers(dna_seq, k_len)
print(f"Maximum Frequency: {max_freq}")
print(f"K-Mers: {max_kmers}")

