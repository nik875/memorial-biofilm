import os
from Bio import SeqIO


def align(input, output, clw=False):
    if clw:
        os.system(f"muscle -in {input} -out {output} -clw")
    else:
        os.system(f"muscle -in {input} -out {output}")


gene_path = "/ncbi_dataset/data/gene.fna"
methanococcus_path = "Data/Sample 16s/Methanococcus maripaludis/"
trichomonas_path = "Data/Sample 16s/Trichomonas vaginalis/"
methanococcus_dirs = next(os.walk(methanococcus_path))[1]
trichomonas_dirs = next(os.walk(trichomonas_path))[1]
methanococcus_seqs = [next(SeqIO.parse(methanococcus_path + i + gene_path, "fasta")) for i in methanococcus_dirs]
trichomonas_seqs = [next(SeqIO.parse(trichomonas_path + i + gene_path, "fasta")) for i in trichomonas_dirs]
with open("methanococcus_seqs.fa", "w") as f:
    SeqIO.write(methanococcus_seqs, f, "fasta")
with open("trichomonas_seqs.fa", "w") as f:
    SeqIO.write(trichomonas_seqs, f, "fasta")
with open("combined_seqs.fa", "w") as f:
    SeqIO.write(methanococcus_seqs + trichomonas_seqs, f, "fasta")
align("methanococcus_seqs.fa", "methanococcus_aln.fa")
align("trichomonas_seqs.fa", "trichomonas_aln.fa")
align("combined_seqs.fa", "combined_aln.fa")
