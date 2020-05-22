# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
# Imports
from Bio import Entrez
from Bio import SeqIO

#############################
# Retrieve NCBI Data Online #
#############################

Entrez.email    = "ehwintermute@gmail.com"    
search_term = 'Staphylococcus aureus subsp. aureus NCTC 8325 CP000253.1'
handle = Entrez.esearch(db='nucleotide', term=search_term)
genome_ids = Entrez.read(handle)['IdList']

for genome_id in genome_ids:
    record = Entrez.efetch(db="nucleotide", id=genome_id, rettype="gb", retmode="text")

    filename = 'genBankRecord_{}.gb'.format(genome_id)
    print('Writing:{}'.format(filename))
    with open(filename, 'w') as f:
        f.write(record.read())
