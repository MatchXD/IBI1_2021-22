import re
seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
enzyme_cuts = re.findall('GAATTC',seq)
num = len(enzyme_cuts)
print('the total number of fragments into which this sequence would be cut if we applied the EcoRI enzyme to it is ',num)
