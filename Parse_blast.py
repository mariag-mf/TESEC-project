from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
import glob
for file in glob.glob("*.xml"):
    with open(file, 'r') as f:
        blast_records = NCBIXML.parse(f)
        for rec in blast_records:
            print('***-***-***-***-***-***-***-***')
            print(f.name)
            for alignment in rec.alignments:
                for hsp in alignment.hsps:
                    if hsp.expect<0.001:
                        print('****Alignment****')
                        print('coverage:', hsp.align_length / rec.query_length)
                        print('identitity:', hsp.identities/ hsp.align_length)
                        '''print(alignment.hit_id)
                        print(alignment.accession)
                        print('sequence:', alignment.title) 
                        print('length:', alignment.length)
                        print('score:', hsp.score)
                        print('gaps:', hsp.gaps)
                        print('e value:', hsp.expect)
                        print('cover:', hsp.qcov_hsp_perc)
                        print(hsp.query[0:90] + '...')
                        print(hsp.match[0:90] + '...')
                        print(hsp.sbjct[0:90] + '...')'''

