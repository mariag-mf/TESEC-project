from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
for record in SeqIO.parse("7_genes.fasta", "fasta"):
    print(record.description[10:23])
    file_name=record.description[10:23]
    fasta_string = record.seq #if you want to read from file
    result = NCBIWWW.qblast("blastp", "nr", fasta_string, ncbi_gi= 'TRUE', expect=0.001, entrez_query='Escherichia coli MG1655', hitlist_size=4)
#saving the blast result
    filename='blast{}.xml'.format(file_name)
    with open(filename, 'w') as f:
        f.write(result.read())
        f.close
        result.close
