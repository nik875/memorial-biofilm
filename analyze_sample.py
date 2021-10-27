import os
from Bio import SeqIO
from Bio.Align.Applications import MuscleCommandline
from ete3 import PhyloTree


muscle_exe = "C:\\Users\\1767709\\bin\\muscle3.8.31_i86win32.exe"
gene_path = "\\ncbi_dataset\\data\\gene.fna"
methanococcus_path = "Data\\Sample 16s\\Methanococcus maripaludis\\"
trichomonas_path = "Data\\Sample 16s\\Trichomonas vaginalis\\"
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
os.system(str(MuscleCommandline(muscle_exe, input="methanococcus_seqs.fa", out="methanococcus_aln.fa")))
os.system(str(MuscleCommandline(muscle_exe, input="trichomonas_seqs.fa", out="trichomonas_aln.fa")))
os.system(str(MuscleCommandline(muscle_exe, input="combined_seqs.fa", out="combined_aln.fa")))
