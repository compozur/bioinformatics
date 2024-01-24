from Bio import SeqIO

def read_fasta(file_path, fmt="fasta"):
    with open(file_path) as handle:
        for record in SeqIO.parse(handle, fmt):
            print(record.id)
            print(record.seq)
            print(len(record))
            print(record.reverse_complement().seq)
            
fasta_file = "example.fasta"
read_fasta(fasta_file)

